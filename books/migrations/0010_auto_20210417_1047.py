# Generated by Django 3.1.6 on 2021-04-17 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
