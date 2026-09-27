from django.urls import re_path
from . import views

urlpatterns=[
    #re_path(r'^', views.index, name='index'),
    re_path(r'^index2/', views.index2, name='index3'),
    re_path(r'^choices/', views.choices, name='choices'),
    re_path(r'^$', views.index,name='index'),
    re_path(r'^logout/', views.logout,name='logout'),
    ]