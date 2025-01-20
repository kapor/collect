from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include
from collection import views

app_name = 'collection'

urlpatterns = [
    # path('books/', views.books, name='index'),
    # path('books/admin', views.books_admin, name='books_admin'),
    path('entry/', views.entry, name='entry'),
    path('entry/admin', views.entry_admin, name='entry_admin'),

    path('books/admin', views.bookview.BookListAdmin.as_view(), name='list'),
    path('books/', views.bookview.BookListView.as_view(), name='list'),
    path('books/<int:pk>/', views.bookview.BookDetailView.as_view(), name='detail'),


    path('update/<int:pk>/', views.edit.update.as_view(), name='update'),
    path('update/<int:pk>/delete', views.edit.delete.as_view(), name='book_delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
