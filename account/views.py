from django.contrib.auth import login
from django.shortcuts import redirect, render

from .forms import RegisterUser


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterUser(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("mytodo:homepage")
    else:
        form = RegisterUser()
    template_name = "registration/sign-up.html"
    context = {"form": form}
    return render(request, template_name, context)
