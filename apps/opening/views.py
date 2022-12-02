from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

header_menu = [
    {"title": "войти", "url_name": "login"},
    {"title": "про нас", "url_name": "#"},
    {"title": "скачать", "url_name": "#"},
    {"title": "блог", "url_name": "#"},
    {"title": "q&a", "url_name": "#"},
]


def index(request: HttpRequest):
    context = {
        "header_menu": header_menu,
        "title": "Чам чакет",
    }
    return render(request, "opening/index.html", context=context)


def login(request: HttpRequest):
    return HttpResponse("Войти")
