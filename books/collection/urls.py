from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.urls import include
from collection import views

app_name = 'collection'

urlpatterns = [
    # path('books/', views.books, name='index'),
    # path('books/admin', views.books_admin, name='books_admin'),
    path('entry/', views.entry, name='entry'),
    path('entry/admin', views.entry_admin, name='entry_admin'),

    path('books/admin', login_required(views.bookview.BookListAdmin.as_view()), name='list'),
    path('books/', login_required(views.bookview.BookListView.as_view()), name='list'),
    path('books/<int:pk>/', login_required(views.bookview.BookDetailView.as_view()), name='detail'),


    path('update/<int:pk>/', login_required(views.edit.update.as_view()), name='update'),
    path('update/<int:pk>/delete', login_required(views.edit.delete.as_view()), name='book_delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
