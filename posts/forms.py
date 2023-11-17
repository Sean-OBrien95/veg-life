from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=150, unique=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
