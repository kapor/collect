from django.db import models
from django.views.generic import ListView
from django.contrib.auth.models import User
# from people.models import UserProfile
from pathlib import Path
import os

def get_upload_path(instance, filename):
    return 'covers/{0}/{1}'.format(instance.user.username, filename)

class BookList(models.Model):
    user = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)
    # id = models.IntegerField(primary_key=True)
    title = models.TextField(max_length=264, blank=True, null=True)
    author = models.TextField(max_length=264, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    type = models.TextField(max_length=264, blank=True, null=True)
    publisher = models.TextField(max_length=264, blank=True, null=True)
    artist = models.TextField(max_length=264, blank=True, null=True)
    quality = models.TextField(max_length=264, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    location = models.TextField(max_length=264, blank=True, null=True)
    genre = models.TextField(max_length=264, blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)
    isbn = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=get_upload_path, default="covers/blank.jpg", blank=True)

    class Meta:
        managed = False
        ordering = ('id',)
        # db_table = 'collection_01'
        verbose_name_plural = "Book Lists"

    def __str__(self):
        return self.title



class BookList2(models.Model):
    user = models.ForeignKey(User, related_name='users2', on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    title = models.TextField(max_length=264, blank=True, null=True)
    author = models.TextField(max_length=264, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    type = models.TextField(max_length=264, blank=True, null=True)
    publisher = models.TextField(max_length=264, blank=True, null=True)
    artist = models.TextField(max_length=264, blank=True, null=True)
    quality = models.TextField(max_length=264, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    location = models.TextField(max_length=264, blank=True, null=True)
    genre = models.TextField(max_length=264, blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)
    isbn = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=get_upload_path, default="covers/blank.jpg", blank=True)

    class Meta:
        managed = False
        ordering = ('id',)
        db_table = 'collect'
        verbose_name_plural = "Book Lists 2"

    def __str__(self):
        return self.title




