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
    context = {"tasks": tasks, "categories": categories}
    return render(request, "cyberpolygon/index.html", context=context)
