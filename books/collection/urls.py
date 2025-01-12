from django.contrib import admin
from django.urls import path
from django.urls import include
from collection import views

app_name = 'collection'

urlpatterns = [
    path('books/', views.books, name='index'),
    path('collection/', views.books, name='collection'),
    path('grid/', views.books, name='grid'),
    path('entry/', views.entry, name='entry'),
    path('entry2/', views.entry2, name='entry2'),
    # path('user_entry/', views.user_entry, name='user_entry'),
    path('update/', views.update.as_view()),
    # path('books/update/<int:id>', views.update, name='update'),
]
