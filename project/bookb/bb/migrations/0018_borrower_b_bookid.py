# Generated by Django 5.0.4 on 2024-07-08 14:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bb', '0017_alter_borrower_b_idnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrower',
            name='b_bookid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bb.book'),
        ),
    ]
