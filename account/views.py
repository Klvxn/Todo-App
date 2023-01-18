from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods

from django_htmx.http import HttpResponseLocation

from .forms import RegisterUser


# Create your views here.
def signup(request):
    if request.method == "POST":
        form = RegisterUser(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("/home/")
    else:
        form = RegisterUser()
    template_name = "registration/sign_up.html"
    context = {"form": form}
    return render(request, template_name, context)


@login_required
@require_http_methods(["DELETE", "POST"])
def delete_todo(request, pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=pk)
    if user == request.user:
        user.delete()
        logout(request)
        return HttpResponseLocation('/')

    return HttpResponseForbidden("<h1> (ERROR!) Request denied.</h1>")
