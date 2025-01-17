from django.db import models
from taggit.managers import TaggableManager
from profiles.models import Bookmarks, Tags
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import admin
from pathlib import Path
import os





def get_upload_path(instance, filename):
    return 'covers/{0}/{1}'.format(instance.user.username, filename)



class BookList(models.Model):
    user = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)
    # id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    author = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=500, blank=True, null=True)
    publisher = models.CharField(max_length=500, blank=True, null=True)
    artist = models.CharField(max_length=500, blank=True, null=True)
    quality = models.CharField(max_length=500, blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)
    location = models.CharField(max_length=500, blank=True, null=True)
    genre = models.CharField(max_length=500, blank=True, null=True)
    tags = TaggableManager(blank=True)
    weight = models.FloatField(blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)
    isbn = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=get_upload_path, default="covers/blank.jpg", blank=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        ordering = ('id',)
        db_table = 'collection_booklist'
        verbose_name_plural = "Book List"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("collection:detail", kwargs={'pk':self.pk})







class BookAdmin(models.Model):
    user = models.ForeignKey(User, related_name='admin', on_delete=models.CASCADE)
    # id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    author = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=500, blank=True, null=True)
    publisher = models.CharField(max_length=500, blank=True, null=True)
    artist = models.CharField(max_length=500, blank=True, null=True)
    quality = models.CharField(max_length=500, blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)
    location = models.CharField(max_length=500, blank=True, null=True)
    genre = models.CharField(max_length=500, blank=True, null=True)
    tags = TaggableManager(blank=True)
    weight = models.FloatField(blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)
    isbn = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=get_upload_path, default="covers/blank.jpg", blank=True)
    notes = models.TextField(blank=True, null=True)
    # tags = models.ManyToManyField(Tags, through='BookAdminTags')

    class Meta:
        managed = False
        ordering = ('id',)
        db_table = 'collection_01'
        verbose_name_plural = "Book Admin"

    def __str__(self):
        return self.title



# class BookAdminTags(models.Model):
#     tags = models.ForeignKey(Tags, on_delete=models.CASCADE)
#     booklist = models.ForeignKey(BookAdmin, on_delete=models.CASCADE)

#     class Meta:
#         ordering = ('tags',)
#         verbose_name_plural = "Tags"



