from django.contrib.auth import login, get_user_model, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods

from .forms import RegisterUser


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterUser(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("mytodo:homepage")

    form = RegisterUser()
    template_name = "registration/sign-up.html"
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
        response = HttpResponse()
        response['HX-Redirect'] = '/'
        return response

    return HttpResponseForbidden("<h1> (ERROR!) Request denied.</h1>")
