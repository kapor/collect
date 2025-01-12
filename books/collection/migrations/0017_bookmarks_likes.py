# Generated by Django 5.1.4 on 2025-01-12 15:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0016_remove_likes_bookmarks_remove_likes_user_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, max_length=264, null=True)),
                ('author', models.TextField(blank=True, max_length=264, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_bm', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Bookmarks',
            },
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genres', models.TextField(blank=True, max_length=264, null=True)),
                ('publishers', models.TextField(blank=True, max_length=264, null=True)),
                ('publications', models.TextField(blank=True, max_length=264, null=True)),
                ('bookmarks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_bookmarks', to='collection.bookmarks')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Likes',
            },
        ),
    ]
