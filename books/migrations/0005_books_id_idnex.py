# Generated by Django 4.0.10 on 2023-03-25 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_books_options'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='books',
            index=models.Index(fields=['id'], name='id_idnex'),
        ),
    ]