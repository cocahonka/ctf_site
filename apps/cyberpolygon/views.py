from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from apps.authorization.models import Profile
from apps.cyberpolygon.models import Task


def opening(request: HttpRequest):
    return render(request, "cyberpolygon/opening.html")


@login_required
def cyberpolygon(request: HttpRequest):
    context = {
        "category_id": 0,
    }
    return render(request, "cyberpolygon/index.html", context=context)


@login_required
def show_task(request: HttpRequest):
    pass


@login_required
def show_category(request: HttpRequest, category_id):
    context = {
        "category_id": category_id,
    }

    return render(request, "cyberpolygon/index.html", context=context)
