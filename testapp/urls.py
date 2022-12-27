
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'testapp'
urlpatterns = [
    path('', views.test_list, name='product_list'),
    path('<slug:category_slug>/', views.test_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.test_detail, name='test_detail'),
    # path('test/', views.test_start, name='test_startt'),





    # url(r'^(?P<category_slug>[-\w]+)/$',
    #     views.product_list,
    #     name='product_list_by_category'),


    # path('', IndexView.as_view(), name='testapp'),
    # re_path(r'^(?P<pk>\d+)/$', PollDetailView.as_view(), name='detail'),
    # re_path(r'^(?P<poll_id>\d+)/vote/$', vote, name='vote'),
    # re_path(r'^(?P<pk>\d+)/results/$', ResultsView.as_view(), name='results'),
]