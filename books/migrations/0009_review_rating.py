# Generated by Django 3.1.6 on 2021-04-15 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20210408_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
