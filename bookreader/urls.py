"""
Bookreader URL Configuration

"""
from django.contrib import admin
from django.urls import path
from . import views
app_name = "boookreader_api"

urlpatterns = [
path('booklist/', views.Books.as_view(), name='books'),

]
