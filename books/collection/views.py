from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from collection.models import BookList
from collection import views, urls
from django.urls import reverse
from django.views.generic import View, TemplateView

from . import forms
import os



# Create your views here.

class update(TemplateView):
    template_name = 'books/update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'Injection'
        return context



def index(request):
    return render(request, 'books/index.html')


def books(request):
    book_list = BookList.objects.order_by('-id')
    book_table = Paginator(book_list, 100)
    page_number = request.GET.get('page')
    try:
        page = book_table.get_page(page_number)
    except PageNotAnInteger:
        page = book_table.page(1)
    except EmptyPage:
        page = book_table.page(book_table.num_pages)
    book_dict = {'book_table':book_list}
    return render(request, 'books/index.html', context={'page_obj':page})


def entry(request):
    form = forms.book_entry()
    if request.method == 'POST':
        form = forms.book_entry(request.POST, request.FILES)  # Note: request.FILES for file uploads
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            photo = form.save()
            return books(request)
    else:
        form = forms.book_entry()
    return render(request, 'entry/user.html',{'form':form})


def entry2(request):
    entry = forms.book_entry2()
    if request.method == 'POST':
        form = forms.book_entry2(request.POST, request.FILES)  # Note: request.FILES for file uploads
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            photo = form.save()
            return books(request)
    else:
        form = forms.book_entry2()
    return render(request, 'entry/auth.html',{'entry2':entry2})


# def update(request, id):
#     form = forms.book_entry()
#     page_obj = BookList.objects.get(id=id)
#     template = loader.get_template('books/update.html')
#     return HttpResponse(template.render(request,{'form':form}))