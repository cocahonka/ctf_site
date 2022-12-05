from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render

from apps.cyberpolygon.models import Category, Task


def opening(request: HttpRequest):
    return render(request, "cyberpolygon/opening.html")


@login_required
def cyberpolygon(request: HttpRequest):
    context = {
        "category_id": 0,
    }
    return render(request, "cyberpolygon/index.html", context=context)


@login_required
def show_task(request: HttpRequest, task_slug):
    task = get_object_or_404(Task, slug=task_slug)

    context = {
        "task": task,
        "category_id": task.category_id,
    }

    return render(request, "cyberpolygon/task.html", context=context)


@login_required
def show_category(request: HttpRequest, category_slug):
    get_object_or_404(Category, slug=category_slug)

    context = {
        "category_slug": category_slug,
    }

    return render(request, "cyberpolygon/index.html", context=context)
