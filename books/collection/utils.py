from django.db import models
from taggit.managers import TaggableManager
from profiles.models import Bookmarks, Tags
from django.views.generic import ListView
from django.contrib.auth.models import User
from pathlib import Path
import os





def comma_splitter(tag_string):
    return [tag.strip() for tag in tag_string.split(',')]