# Generated by Django 5.0.4 on 2024-04-30 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bb', '0012_merge_20240429_2050'),
    ]

    operations = [
        migrations.CreateModel(
            name='LibraryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('due_date', models.DateField()),
            ],
        ),
    ]
