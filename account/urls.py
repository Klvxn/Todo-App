from django.urls import include, path

from . import views


app_name = "account"

urlpatterns = [
    path("auth/", include("django.contrib.auth.urls")),
    path("sign-up/", views.signup, name="register"),
    path('delete/<int:pk>/', views.delete_todo, name="delete")
]
