# Generated by Django 5.1.4 on 2025-01-15 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0022_remove_likes_bookmarks_remove_likes_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Tags',
            },
        ),
    ]