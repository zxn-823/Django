from django.contrib import admin
from django.urls import path
#.代表当前目录，从当前目录导入views模块
from . import views

urlpatterns = [
    #name='index'是给views.index起的一个别名，便于后续的处理
    path('',views.index,name='index'),
]