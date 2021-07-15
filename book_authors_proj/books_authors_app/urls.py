from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
urlpatterns = [
    path('', views.index),
    path('book', views.addBook),
    path('book/<int:number>',views.book),
    path('author', views.indexAuthor),
    path('author/addAuthor', views.addAuthor),
    
]
