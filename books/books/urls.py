"""
URL configuration for books project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from profiles import views
from profiles import urls
from collection import urls
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),

    # path('', views.index, name='index'),

    #class based view
    path('', views.index.as_view()), 
    path('home/', views.home, name='home'),

    path('', include('profiles.urls')),
    path('success/', views.home, name='success_page'),

    path('profiles/', views.people, name='people'),
    path('join/', views.join, name='join'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('loggedin/', views.loggedin, name='loggedin'),

    path('', include('collection.urls')),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



