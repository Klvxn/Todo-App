from django.shortcuts import redirect, render
from django.contrib.auth import login

from .forms import RegisterUser


# Create your views here.
def register(request):
    form = RegisterUser()
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('mytodo:homepage')
    else:
        form = RegisterUser()
    context = {'form': form}
    return render(request, 'registration/sign-up.html', context)