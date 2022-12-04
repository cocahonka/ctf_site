from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import UserRegisterForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"{username} Ваш аккаунт создан: можно войти на сайт.")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "authorization/register.html", {"form": form})


@login_required
def profile(request):
    return render(request, "authorization/profile.html")
