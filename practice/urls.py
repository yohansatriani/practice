"""practice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from practice.views import hello, boot, main, current_datetime, present_time, open_time, right_time, in_time, short_time, hours_ahead, login, film_list, request_data, meta_data, contact
from books.views import search_form, search

urlpatterns = [
    #admin
    path('admin/', admin.site.urls),
    #basictemplate
    path('boot/', boot),
    path('main/', main),
    #basic
    path('hello/', hello),
    path('time/', current_datetime),
    path('anothertime/', current_datetime),
    path('presenttime/', present_time),
    path('opentime/', open_time),
    path('righttime/', right_time),
    path('intime/', in_time),
    path('shorttime/', short_time),
    path('time/plus/<int:offset>/', hours_ahead),
    #request
    path('reqdata/', request_data),
    path('metadata/', meta_data),
    #form
    path('searchform/', search_form),
    path('search/', search),
    #login
    path('login/', login),
    #model+template
    path('film/', film_list),
    #form
    path('contact/', contact)
]
