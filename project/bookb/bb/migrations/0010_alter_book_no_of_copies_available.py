# Generated by Django 5.0.4 on 2024-04-28 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bb', '0009_rename_books_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='No_Of_copies_Available',
            field=models.CharField(max_length=30),
        ),
    ]
