from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from apps.authorization.models import Profile
from apps.cyberpolygon.models import Task


def opening(request: HttpRequest):
    return render(request, "cyberpolygon/opening.html")


@login_required
def cyberpolygon(request: HttpRequest):
    profile = Profile.objects.get(user=request.user)
    categories = profile.category.all()
    tasks = Task.objects.filter(category__in=categories, is_published=True)
    context = {
        "tasks": tasks,
        "categories": categories,
        "category_selected": 0,
    }
    return render(request, "cyberpolygon/index.html", context=context)


@login_required
def show_task(request: HttpRequest):
    pass


@login_required
def show_category(request: HttpRequest, category_id):
    profile = Profile.objects.get(user=request.user)
    categories = profile.category.all()
    tasks = Task.objects.filter(category_id=category_id, is_published=True)

    context = {
        "tasks": tasks,
        "categories": categories,
        "category_selected": category_id,
    }

    return render(request, "cyberpolygon/index.html", context=context)
