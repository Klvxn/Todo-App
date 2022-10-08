from django.urls import path

from . import views


app_name = "mytodo"

urlpatterns = [
    path("", views.index, name="indexpage"),
    path("home/", views.home, name="home"),
    path("to-dos/<int:pk>/", views.todo_detail, name="todo-detail"),
    path("to-dos/add/", views.add_todo, name="add-todo"),
    path("to-dos/<int:pk>/edit/", views.edit_todo, name="edit-todo"),
    path("to-dos/<int:pk>/delete/", views.delete_todo, name="delete-todo"),
]
