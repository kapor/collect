from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from collection.models import BookList
from profiles.models import UserInfo
from profiles.forms import UserForm1, UserForm2, BookmarkForm
from . import models, forms
from django.contrib.auth.models import User
from django.views.generic import View, TemplateView, ListView, DetailView
import os


# 
# 
# 




class profile(View):

    class Home(TemplateView):
        context_object_name = 'profile'
        template_name = 'profile/index.html'

    class BookMarksList(ListView):
        model = models.Bookmarks
        context_object_name = 'bookmarks'
        template_name = 'profile/bm_view.html'


    class BookMarksDetail(DetailView):
        model = models.Bookmarks
        context_object_name = 'bookmarks_detail'
        template_name = 'profile/bm_detail.html'


# def bookmarktags(request):
#     if request.method == 'POST':
#         form = BookmarkForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('success_page')
#     else:
#         form = BookmarkForm()
#     return render(request, 'profile/bookmarks.html', {'form': form})


class index(View):
    def get(request):
        table = BookList.objects.order_by('-id')
        paginator = Paginator(table, 100)
        page_number = request.GET.get('page')
        try:
            page = paginator.get_page(page_number)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        page_table = {'paginator':table}
        return render(request, 'books/index.html', context={'page_obj':page})



    def home(request):
        book_list = BookList.objects.order_by('-id')
        book_table = Paginator(book_list, 100)
        page_number = request.GET.get('page')
        try:
            page = book_table.get_page(page_number)
        except PageNotAnInteger:
            page = book_table.page(1)
        except EmptyPage:
            page = book_table.page(book_table.num_pages)
        page_table = {'book_table':book_list}
        return render(request, 'home.html', context={'page_obj':page})


def people(request):
    people_list = UserInfo.objects.order_by('-id')
    people_table = Paginator(people_list, 20)
    page_number = request.GET.get('page')
    try:
        page = people_table.get_page(page_number)
    except PageNotAnInteger:
        page = people_table.page(1)
    except EmptyPage:
        page = people_table.page(people_table.num_pages)
    # context = {'page_obj':page}
    return render(request, 'people/index.html', context={'page_obj':page})



class reg():

    def reg_join(request):

        registered = False

        user_form = UserForm1()
        prof_form = UserForm2()

        if request.method == 'POST':
            user_form = forms.UserForm1(data=request.POST)
            prof_form = forms.UserForm2(data=request.POST)

            if user_form.is_valid() and prof_form.is_valid():

                user = user_form.save()
                user.set_password(user.password)
                user.save()

                profile = prof_form.save(commit=False)
                profile.user = user

                if 'picture' in request.FILES:
                    profile.picture = request.FILES['picture']

                profile.save()

                registered = True
                login(request, user)
                return HttpResponseRedirect(reverse('success_page'))
                
            else:
                print(user_form.errors, prof_form.errors)

        else:
            user_form = UserForm1()
            prof_form = UserForm2()

        return render(request, 'reg/join.html',{'user_form':user_form, 'prof_form':prof_form, 'registered':registered})

    def reg_login(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('success_page'))
                else:
                    return HttpResponse("Account not active")
            else: 
                print("Failed login")
                print("username: {} and password {}".format(username,password))
                return HttpResponse("Invalid Login")
        else:
            return render(request, 'reg/login.html', {})


    @login_required #decorator
    def reg_loggedin(request):
        logout(request)
        return render(request, 'base/user.html', {})

    @login_required #decorator
    def reg_logout(request):
        logout(request)
        return render(request, 'reg/login.html', {})





# def reg(request):
#     form = user_entry()

#     if request.method == 'POST':
#         form = forms.user_entry(request.POST)

#         if form.is_valid():
#             form.save(commit=True)
#             # DO SOMETHING CODE
#             print('working')
#             print("NAME: "+form.cleaned_data['name'])
#             return people(request)
#         else:
#             print('NOT GOOD')
#     return render(request, 'reg/join.html',{'form':form})









