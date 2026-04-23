from django.contrib import admin
from django.urls import path,include,re_path
from .views import *


urlpatterns = [
    path("", login_page),    # Login page
    path("home/",helloView),
    path("add-book/",addBookView),
    path("add-book/add",addBook),
    path("edit-book/",editBookView),
    path("edit-book/edit",editBook),
    path("delete-book",deleteBookView),
    path('register/', register_page, name='register'),# Registration page
]