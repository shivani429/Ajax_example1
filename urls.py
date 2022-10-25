from django.contrib import admin
from django.urls import path
from . import views
from demoapp.views import *
urlpatterns = [
    
    path('profile', views.profile, name='profile'),
    path('getprofile', views.getprofile, name='getprofile'),
    path('create', views.create, name='create'),
   
]
