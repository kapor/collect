from django.db import models
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.core.validators import URLValidator
from pathlib import Path
import os

# Create your models here.


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to="profile_pics/", default="", blank=True)

	class Meta:
		managed = False
		ordering = ('id',)
		verbose_name_plural = "User Profiles"

	def __str__(self):
   		return self.user.username



