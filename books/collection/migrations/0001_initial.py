# Generated by Django 5.1.4 on 2025-01-11 21:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BookList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, max_length=264, null=True)),
                ('author', models.TextField(blank=True, max_length=264, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('type', models.TextField(blank=True, max_length=264, null=True)),
                ('publisher', models.TextField(blank=True, max_length=264, null=True)),
                ('artist', models.TextField(blank=True, max_length=264, null=True)),
                ('quality', models.TextField(blank=True, max_length=264, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('location', models.TextField(blank=True, max_length=264, null=True)),
                ('genre', models.TextField(blank=True, max_length=264, null=True)),
                ('weight', models.FloatField(blank=True, null=True)),
                ('pages', models.IntegerField(blank=True, null=True)),
                ('isbn', models.FloatField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, default='covers/blank.jpg', upload_to='covers/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
