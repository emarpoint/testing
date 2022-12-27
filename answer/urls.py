
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import *

app_name = 'answer'
urlpatterns = [
    path('test/', views.test_start, name='test_start'),
    path('result/', views.test_start, name='test_result'),


]
  
