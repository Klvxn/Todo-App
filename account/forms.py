from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Forms
class RegisterUser(UserCreationForm):
    username = forms.CharField(
        max_length=10, help_text="Letters, digits and @/./+/-/_ only."
    )
    password1 = forms.CharField(
        label="Password",
        min_length=8,
        widget=forms.PasswordInput(),
        help_text="Password must contain at least 8 characters."
    )
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
