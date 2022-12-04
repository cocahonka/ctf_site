from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def save(self, *args, **kwargs):
        user = super(UserRegisterForm, self).save(*args, **kwargs)
        Profile.objects.create(user=user)
