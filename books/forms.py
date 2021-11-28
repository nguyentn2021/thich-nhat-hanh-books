from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Book
from django.core.exceptions import ValidationError

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class AddBookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'



  
#test form created by me for more handsome --> get errors! give up :()
class MyAddBookForm(AddBookForm):

    class Meta:
        model = Book
        fields = '__all__'

    name = forms.CharField(
                    max_length=300, 
                    widget=forms.Textarea(
                        attrs={
                            "rows":1,
                            "cols":80
                        }
                    )
                    )
    image = forms.ImageField()
    summary = forms.CharField(
                    required=False,
                    widget=forms.Textarea(
                        attrs={
                            "rows":10,
                            "cols":120
                        }
                    )
    )
    publication_date = forms.DateField()


    