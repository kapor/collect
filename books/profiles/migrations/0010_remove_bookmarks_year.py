# Generated by Django 5.1.4 on 2025-01-12 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmarks',
            name='year',
        ),
    ]
