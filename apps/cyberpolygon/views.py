from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest):
    return render(request, "cyberpolygon/index.html")


def login(request: HttpRequest):
    return HttpResponse("Войти")
