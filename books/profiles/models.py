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