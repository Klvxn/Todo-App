from django.urls import path

from . import views

app_name = 'mytodo'

urlpatterns = [
    path('', views.indexpage, name='indexpage'),
    path('home/', views.homepage, name='homepage'),
    path('todos/<int:pk>/', views.detailpage, name='detailpage'),
    path('todos/create-todo/', views.create_todo, name='create-todo'),
    path('todos/<int:pk>/edit-todo/', views.edit_todo, name='edit-todo'),
    path('todos/<int:pk>/delete-todo/', views.delete_todo, name='delete-todo'),
    path('todos/completed-todos/', views.completed_todos, name='completed-todos'),
    path('todos/uncompleted-todos/', views.uncompleted_todos, name='uncompleted-todos'),

]