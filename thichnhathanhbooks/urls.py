"""thichnhathanhbooks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import books.views
from django.conf import settings
from django.conf.urls.static import static
from books.views import BookDetail, BookReview, AddBook, BookListView

urlpatterns = [
    path('register/', books.views.register_page, name='register_page'),
    path('login/', books.views.login_page, name='login_page'),
    path('logout/', books.views.logout_user, name='logout_user'),
    path('', books.views.home, name='home'),
    path('admin/', admin.site.urls),
    path('', books.views.home, name='home'),
    path('books/<int:book_id>/', books.views.BookDetail.as_view(), name='book_detail'),
    path('review/<int:book_id>/', books.views.BookReview.as_view(), name='book_review'),
    #path('list/', books.views.BookListView.as_view(), name='book_list'),
    path('add/', books.views.AddBook, name='add'),
    #path('update/<int:book_id>', books.views.UpdateBook, name='update'),
    path('update/<int:book_id>', books.views.UpdateBookClass.as_view(), name='update'),
    path('delete/<int:book_id>', books.views.DeleteBook, name='delete'),
    path('list/', books.views.book_list_2, name='book_list'),
    
] 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


