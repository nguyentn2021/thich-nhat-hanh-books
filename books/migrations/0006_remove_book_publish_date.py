# Generated by Django 3.1.6 on 2021-03-21 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_book_publish_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='publish_date',
        ),
    ]
