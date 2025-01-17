from django.contrib import admin
from collection.models import BookList, BookAdmin
# Register your models here.

admin.site.register(BookList)
admin.site.register(BookAdmin)

