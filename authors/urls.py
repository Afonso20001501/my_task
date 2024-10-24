
from django.shortcuts import render
from django.urls import path
from . import views

app_namee = 'authors'

urlpatterns = [
    path('register/', views.AuthorView.as_view(), name='author-register')
]
