# Generated by Django 3.1.6 on 2021-03-13 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bool_title', models.CharField(default='', max_length=300)),
                ('review_summary', models.TextField()),
                ('reviewer', models.CharField(max_length=100)),
            ],
        ),
    ]
