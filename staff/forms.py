from django.forms import ModelForm, TextInput, Textarea, Select, NumberInput, FileInput, CharField, PasswordInput
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import *


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    widgets = {
        "password": PasswordInput(attrs={
            'placeholder': "Password",
            'required': ""
        }),
    }


class ChangePassword(UserCreationForm):
    class Meta:
        model = User
        fields = ('password', )

    widgets = {
        "password": PasswordInput(attrs={
            'placeholder': "Password",
            'required': ""
        })
    }
