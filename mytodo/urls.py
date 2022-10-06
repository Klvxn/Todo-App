from django.urls import path

from . import views


app_name = "mytodo"

urlpatterns = [
    path("", views.indexpage, name="indexpage"),
    path("home/", views.homepage, name="homepage"),
    path("to-dos/<int:pk>/", views.detailpage, name="detailpage"),
    path("to-dos/add-todo/", views.create_todo, name="add-todo"),
    path("to-dos/<int:pk>/edit-todo/", views.edit_todo, name="edit-todo"),
    path("to-dos/<int:pk>/delete-todo/", views.delete_todo, name="delete-todo"),
]
