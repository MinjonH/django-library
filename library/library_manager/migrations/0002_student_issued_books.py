# Generated by Django 4.1.7 on 2023-03-19 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='issued_books',
            field=models.IntegerField(default=0),
        ),
    ]
