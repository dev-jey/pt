from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect

urlpatterns = [
    path('', views.get_home, name='home'),
    path('project/<int:id>', views.get_project, name='project-view'),
]
