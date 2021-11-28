from django.shortcuts import render, redirect
from .models import Book, Review
from django.views.generic.base import View, TemplateView
from django.http import response
from django.template.response import SimpleTemplateResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, AddBookForm, MyAddBookForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.contrib import messages


@login_required(login_url='login/')
def home(request):
    books = Book.objects
    return render(request, 'home.html', {'books':books})

def register_page(request):
    
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' +  user)
            return redirect('login_page')

    context = {'form':form}

    return render(request, 'register.html', context)

def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR Password is incorrect!')
           
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('login_page')


class BookDetail(View):

    def get(request, *args, **kwargs):
        
        book_id = kwargs.get('book_id')
        book = Book.objects.get(id=book_id)
        review = Review.objects.filter(title_id=book_id)
    
        context = {
            'book':book,
            'review': review
        }

        return SimpleTemplateResponse ('book_detail.html', context)
    

class BookReview(TemplateView):  

    template_name = 'review.html'

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
            
        book_id = kwargs.get('book_id')
        review = Review.objects.filter(title_id=book_id)
        book = Book.objects.get(id=book_id)

        context['book'] = book
        context['review'] = review
        
        return context
        
   
    def post(self, request, **kwargs):
        
        context = self.get_context_data(**kwargs)
        #content = request.POST['content']
        #rating = request.POST['rating']
        context['review'].content = request.POST['content']
        context['review'].rating = request.POST['rating']
        
        book_id = kwargs.get('book_id')
        current_book = Book.objects.get(id=book_id)
        
        new_review = Review.objects.create(title=current_book)
        new_review.author=request.user.username
        new_review.content=request.POST['content']
        new_review.rating=request.POST['rating']
        new_review.save()

        return render (request, self.template_name, context)
    

class BookListView(ListView):

    template_name = 'book_list.html'
    model = Book
    paginate_by = 100  # if pagination is desired

def book_list_2(request):

    books = Book.objects.all()
    return render(request, 'book_list2.html', {'books':books})


@login_required(login_url='login/')
def AddBook(request):
    
    form = MyAddBookForm()
    
    if request.method == "POST":

        form = MyAddBookForm(request.POST,request.FILES)     
        
        if form.is_valid():
            form.save()
            return redirect('home')

    context={
        'form':form
    }
    return render (request, 'add_book.html' , context)
        

@login_required(login_url='login/')
def UpdateBook(request, book_id):

    book = Book.objects.get(id=book_id)
    form = AddBookForm(instance=book)
    
    context={
        'form':form,
        'book':book
    }
    
    if request.method == "POST":
        form = AddBookForm(request.POST,request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return SimpleTemplateResponse ('book_detail.html', context)

    return render (request, 'add_book.html' , context)

        
@login_required(login_url='login/')
def DeleteBook(request, book_id):
    
    book = Book.objects.get(id=book_id)
    
    if request.method == "POST":
        book.delete()
        return redirect('home')
    
    context={'book':book}
    
    return render (request, 'delete.html' , context)


class UpdateBookClass(TemplateView):
    
    template_name = 'add_book.html'

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
            
        book_id = kwargs.get('book_id')
        review = Review.objects.filter(title_id=book_id)
        book = Book.objects.get(id=book_id)

        context['book'] = book
        context['review'] = review
        context['form'] = MyAddBookForm(instance=book)
        
        return context
        
    
    def post(self, request, **kwargs):
        
        context = self.get_context_data(**kwargs)
        book = context['book']

        #form = MyAddBookForm(data=request.POST)
        form = MyAddBookForm(request.POST,request.FILES, instance=book)

        if form.is_valid():      
        #    book.name=form.cleaned_data['name']
        #    book.image=form.cleaned_data['image']
        #    book.summary=form.cleaned_data['summary']
        #    book.publication_date=form.cleaned_data['publication_date']
            form.save()
            return render (request, 'book_detail.html', context)
        else:
            return render (request, self.template_name, context)