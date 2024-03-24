"""
URL configuration for project_jam project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from jam import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('contact.html', views.contact, name='contact'),
    path('partager.html', views.partager, name='partager'),
    path('partager.html', views.partager_histoire, name='partager_histoire'),
    path('mission_list.html', views.mission_list, name='mission_list'),
    path('mission_detail/<int:pk>/', views.mission_detail, name='mission_detail'),
    path('mission/new/', views.mission_new, name='mission_new'),
    path('mission_edit.html', views.mission_edit, name='mission_edit'),
    path('mission_delete.html', views.mission_delete, name='mission_delete'),
]
