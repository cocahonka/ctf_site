from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from apps.cyberpolygon.models import Category

from .models import *


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Категория (1-3)",
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "category"]

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields["category"].error_messages = {"required": "Обязательно выбрать хотя бы 1 категорию"}

    def save(self, *args, **kwargs):
        user = super(UserRegisterForm, self).save(commit=False, *args, **kwargs)
        user._category = self.cleaned_data["category"]
        user.save()

    def clean_category(self):
        value = self.cleaned_data["category"]
        if len(value) > 3:
            raise forms.ValidationError("Нелья выбрать больше 3 категорий")
        return value
