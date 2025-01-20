from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from collection.models import BookList, BookAdmin
from collection import views, urls
from django.urls import reverse, reverse_lazy
from django.views.generic import View, TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from . import models, forms
import os



# Create your views here.

class edit(View):

    class update(UpdateView):
        template_name = 'books/update.html'
        model = models.BookList
        form_class = forms.book_update
        context_object_name = 'book_update'
        success_url = reverse_lazy("collection:list")


    class delete(DeleteView):
        model = models.BookList
        template_name = 'books/delete.html'
        context_object_name = 'book_delete'
        success_url = reverse_lazy("collection:list")

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['injectme'] = 'Update'
    #     return context







class bookview(View):

    class BookListView(ListView):
        model = models.BookList
        context_object_name = 'booklist'
        template_name = 'books/book_list.html'
        paginate_by = 20
        queryset = BookList.objects.order_by('-id')
        #Below filters items only created by the logged-in user
        def get_queryset(self):
            return super().get_queryset().filter(user=self.request.user)

    class BookDetailView(DetailView):
        model = models.BookList
        context_object_name = 'bookdetail'
        template_name = 'books/book_detail.html'

    class BookListAdmin(ListView):
        model = models.BookAdmin
        context_object_name = 'bookadmin'
        template_name = 'books/admin.html'
        paginate_by = 100
        queryset = BookAdmin.objects.order_by('-id')
        def get_queryset(self):
            return super().get_queryset().filter(user=self.request.user)




def entry(request):
    form = forms.book_entry()
    if request.method == 'POST':
        form = forms.book_entry(request.POST, request.FILES)  
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            photo = form.save()
            form.save_m2m()
            return redirect('/books/')
    else:
        form = forms.book_entry()
    return render(request, 'entry/create.html',{'form':form})

# CLASS BASED VIEW - SAME AS ABOVE
# class create_entry(CreateView):
#     template_name = 'entry/create.html'
#     model = models.BookList
#     fields = ('title', 'author' , 'year', 'type', 'publisher', 'artist', 'quality', 'price', 'location', 'genre', 'tags', 'weight', 'pages', 'isbn', 'description', 'notes', 'image')





def entry_admin(request):

    form2 = forms.book_admin()
    if request.method == 'POST':
        form2 = forms.book_admin(request.POST, request.FILES)  
        if form2.is_valid():
            profile = form2.save(commit=False)
            profile.user = request.user
            profile.save()
            photo = form2.save()
            return redirect('/books/admin')
    else:
        form = forms.book_admin()
    return render(request, 'entry/admin.html',{'form2':form2})

# CLASS BASED VIEW - SAME AS ABOVE
# class create_entry_admin(CreateView):
#     template_name = 'entry/create.html'
#     model = models.BookAdmin
#     fields = ('title', 'author' , 'year', 'type', 'publisher', 'artist', 'quality', 'price', 'location', 'genre', 'tags', 'weight', 'pages', 'isbn', 'description', 'notes', 'image')














