from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def opening(request: HttpRequest):
    return render(request, "cyberpolygon/opening.html")


def cyberpolygon(request: HttpRequest):
    return render(request, "cyberpolygon/index.html")
