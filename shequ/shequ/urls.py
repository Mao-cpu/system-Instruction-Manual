"""shequ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.blog_login,name='blog_login'),
    path('person/', views.blog_list, name='blog_list'),
    path('p_i/', views.p_i,name='p_i'),
    path('edit/', views.blog_edit, name='blog_edit'),
    path('register/', views.register, name='register'),
    path('index/', views.index, name='index'),
    path('resource/', views.resource, name='resource'),
    path('info/list/', views.info_list,name='info_list'),
    path('info/delete/', views.info_delete),
    path('page_list/',views.page_list,name='page_list'),
    path('page_add/', views.page_add, name='page_add'),
    path('info/delete1/', views.info_delete1),
    path('info/delete2/', views.info_delete2),
    path('mindex/', views.mindex,name='mindex'),
    path('mblog_list/', views.mblog_list,name='mblog_list'),
    path('pindex/', views.pindex,name='pindex'),
    path('plist/', views.plist,name='plist'),
    path('pedit/', views.pedit,name='pedit'),
    path('nlist/', views.nlist,name='nlist'),
    path('nedit/', views.nedit,name='nedit'),
    path('community/', views.community,name='community'),
    path('fp/', views.fp,name='fp'),
]
