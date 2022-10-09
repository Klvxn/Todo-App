from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Forms
class RegisterUser(UserCreationForm):
    
    username = forms.CharField(min_length=3)

    password1 = forms.CharField(
        label="Password",
        min_length=8,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
