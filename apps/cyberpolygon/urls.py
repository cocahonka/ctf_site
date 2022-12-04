from django.urls import path

from . import views

urlpatterns = [
    path("", views.opening, name="home"),
    path("cyberpolygon/", views.cyberpolygon, name="cyberpolygon"),
]
