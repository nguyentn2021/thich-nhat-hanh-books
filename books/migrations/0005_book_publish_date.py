# Generated by Django 3.1.6 on 2021-03-21 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20210321_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publish_date',
            field=models.DateField(default='1900-01-01'),
            preserve_default=False,
        ),
    ]
