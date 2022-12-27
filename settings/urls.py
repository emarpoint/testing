
from django.contrib import admin
from django.urls import path, include
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),

    # path('api-auth/', include('rest_framework.urls')),
    path('testapp/', include('testapp.urls', namespace="testapp"), ),
    path('answer/', include('answer.urls', namespace="answer"), ),


]
