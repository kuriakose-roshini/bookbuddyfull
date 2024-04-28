# Generated by Django 5.0.4 on 2024-04-28 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bb', '0005_books'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='Author',
            new_name='Name_of_Author',
        ),
        migrations.RenameField(
            model_name='books',
            old_name='Num_copy',
            new_name='No',
        ),
        migrations.RenameField(
            model_name='books',
            old_name='B_name',
            new_name='Title',
        ),
        migrations.AddField(
            model_name='books',
            name='No_Of_copies_Available',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
