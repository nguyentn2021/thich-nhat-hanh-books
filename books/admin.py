from django.contrib import admin
from .models import Book, Review

class BookAdmin(admin.ModelAdmin):
   list_display = ['name','publication_date']

admin.site.register(Book,BookAdmin)

class ReviewAdmin(admin.ModelAdmin):
   list_display = ['title','content','rating','author','created','last_updated']

admin.site.register(Review,ReviewAdmin)
