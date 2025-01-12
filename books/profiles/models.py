from django.db import models
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.core.validators import URLValidator
from pathlib import Path
import os

# Create your models here.

def get_upload_path(instance, filename):
    return 'profile_pics/{0}/{1}'.format(instance.user.username, filename)


class UserInfo(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to=get_upload_path, default="blank.jpg", blank=True)

	class Meta:
		# managed = False
		# ordering = ('id',)
		verbose_name_plural = "Info"

	def __str__(self):
   		return self.user.username



class Bookmarks(models.Model):
    user = models.ForeignKey(User, related_name='user_bm', on_delete=models.CASCADE) 
    title = models.TextField(max_length=264, blank=True, null=True)
    author = models.TextField(max_length=264, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Bookmarks"

    def __str__(self):
        return self.title



class Likes(models.Model):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE) 
    genres = models.TextField(max_length=264, blank=True, null=True)
    publishers = models.TextField(max_length=264, blank=True, null=True)
    publications = models.TextField(max_length=264, blank=True, null=True)
    bookmarks = models.ForeignKey(Bookmarks, related_name='user_bookmarks', on_delete=models.CASCADE) 

    class Meta:
        verbose_name_plural = "Likes"

    def __str__(self):
        return self.genres