from django.contrib import admin
from django.urls import path, include, reverse
from django.conf.urls.static import static
from django.conf import settings
from . import views


app_name = 'profiles'

urlpatterns = [
    path('', views.index.home, name='index'),
    path('profile/', views.profile.Home.as_view(), name='profile'),
    path('bookmarks/', views.profile.BookMarksList.as_view(), name='list'),
    path('bookmarks/<int:pk>/', views.profile.BookMarksDetail.as_view(), name='detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
