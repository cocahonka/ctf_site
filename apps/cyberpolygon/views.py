from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .decorators import *


def opening(request):
    return render(request, "cyberpolygon/opening.html")


@login_required
def cyberpolygon(request):
    context = {
        "categories": request.user.profile.category.all(),
    }
    return render(request, "cyberpolygon/index.html", context=context)


@login_required
@categories_match_required()
def show_category(request, category_slug, **kwargs):
    context = {
        "category_slug": category_slug,
        "category": kwargs.get("category"),
        "categories": kwargs.get("categories"),
    }

    return render(request, "cyberpolygon/index.html", context=context)


@login_required
@categories_match_required(task_filters=dict(is_published=True))
def show_task(request, **kwargs):
    task = kwargs.get("task")

    context = {
        "task": task,
        "categories": kwargs.get("categories"),
    }

    return render(request, "cyberpolygon/task.html", context=context)
