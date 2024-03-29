from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Your username",
        "class": "w-full p-3 rounded"
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Your password",
        "class": "w-full p-3 rounded"
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "johnsmith",
        "class": "w-full p-3 rounded"
    }))
    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "placeholder": "john@example.com",
        "class": "w-full p-3 rounded"
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Enter your desired password",
        "class": "w-full p-3 rounded"
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Retype your desired password",
        "class": "w-full p-3 rounded"
    }))
