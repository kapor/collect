from django.contrib import admin
from django.urls import path
from django.urls import include
from profiles import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'profiles'

urlpatterns = [
    path('', views.people, name='people'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
