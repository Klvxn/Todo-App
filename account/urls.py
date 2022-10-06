from django.urls import include, path

from . import views


app_name = "account"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("sign-up/", views.register, name="register"),
    path('delete-account/<int:pk>/', views.delete_todo, name="delete")
]
