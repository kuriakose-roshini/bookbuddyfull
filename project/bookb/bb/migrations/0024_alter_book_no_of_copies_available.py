# Generated by Django 5.0.4 on 2024-07-21 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bb', '0023_remove_book_no_of_copies_available_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='No_of_Copies_Available',
            field=models.CharField(max_length=30),
        ),
    ]