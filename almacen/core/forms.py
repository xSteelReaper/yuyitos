from django import forms
from django.core import validators

from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']