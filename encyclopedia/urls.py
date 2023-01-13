from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("newPage/", views.newPage, name="newPage"),
    path("edit/", views.edit, name="edit"),
    path("saveEdit/", views.saveEdit, name="saveEdit"),
    path("randomEntry/", views.randomEntry, name="randomEntry"),
    path("delete", views.delete, name="delete"),
    
]
