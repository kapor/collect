from django.contrib import admin
from profiles.models import UserInfo, Bookmarks, Likes
# Register your models here.
admin.site.register(UserInfo)
admin.site.register(Bookmarks)
admin.site.register(Likes)

