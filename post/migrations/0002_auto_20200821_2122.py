# Generated by Django 3.1 on 2020-08-21 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Slug',
            new_name='slug',
        ),
    ]