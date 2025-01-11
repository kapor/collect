from django.contrib import admin
from django.urls import path
from django.urls import include
from people import views

app_name = 'people'

urlpatterns = [
    path('', views.people, name='people'),

]
