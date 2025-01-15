from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from collection.models import BookList, BookAdmin
from collection import views, urls
from django.urls import reverse
from django.views.generic import View, TemplateView, ListView, DetailView, FormView
from . import models, forms
import os



# Create your views here.

class update(TemplateView):
    template_name = 'books/update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'Injection'
        return context


# class BookDetailView(DetailView):
#     model = models.BookList
#     context_object_name = 'book_detail'
#     template_name = 'books/book_detail.html'







class bookview(View):

    class BookListView(ListView):
        model = models.BookList
        context_object_name = 'booklist'
        template_name = 'books/book_list.html'
        paginate_by = 20
        queryset = BookList.objects.order_by('-id')

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
        # new method added ⬇️
        # def get_template_names(self, *args, **kwargs):
        #     if self.request.htmx:
        #         return "books/admin.html"
        #     else:
        #         return self.template_name









# def books(request):
#     table = BookList.objects.order_by('-id')
#     paginator = Paginator(table, 100)
#     page_number = request.GET.get('page')
#     try:
#         page = paginator.get_page(page_number)
#     except PageNotAnInteger:
#         page = paginator.page(1)
#     except EmptyPage:
#         page = paginator.page(paginator.num_pages)
#     book_dict = {'book_table':table}
#     return render(request, 'books/index.html', context={'page_obj':page})


# def books_admin(request):
#     table = BookAdmin.objects.order_by('-id')
#     paginator = Paginator(table, 200)
#     page_number = request.GET.get('page')
#     try:
#         page = paginator.get_page(page_number)
#     except PageNotAnInteger:
#         page = paginator.page(1)
#     except EmptyPage:
#         page = paginator.page(paginator.num_pages)
#     book_dict = {'paginator':table}
#     return render(request, 'books/admin.html', context={'page_obj':page})



# class entry_form(FormView):
#     template_name = "entry/user.html"
#     form_class = book_entry
#     success_url = "success_page/"


def entry(request):
    form = forms.book_entry()
    if request.method == 'POST':
        form = forms.book_entry(request.POST, request.FILES)  
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            photo = form.save()
            return redirect('/books/')
    else:
        form = forms.book_entry()
    return render(request, 'entry/user.html',{'form':form})


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








