from django.contrib import admin
from django.urls import path
from django.urls import include
from collection import views

app_name = 'collection'

urlpatterns = [
    path('books/', views.books, name='index'),
    path('collection/', views.books, name='collection'),
    path('grid/', views.books, name='grid'),
    path('books/admin', views.books_admin, name='books_admin'),
    path('entry/', views.entry, name='entry'),
    path('entry/admin', views.entry_admin, name='entry_admin'),
    path('update/', views.update.as_view()),
    # path('books/update/<int:id>', views.update, name='update'),
    path('', views.update.as_view())

]
