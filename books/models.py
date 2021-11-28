from django.db import models

# Create your models here.
class Book(models.Model):
    image = models.ImageField(upload_to='')
    name = models.CharField(max_length=300, default='')
    summary = models.TextField(blank=False, null=False)
    publication_date = models.DateField(default='1900-01-01')

    def __str__(self):
       return self.name

class Review(models.Model):
    title = models.ForeignKey(to=Book, related_name='title_name', on_delete=models.CASCADE,null=True, blank=True)
    content = models.TextField(blank=False, null=False)
    rating = models.CharField(max_length=255, null=True)
    author = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
