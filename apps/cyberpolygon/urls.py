from django.urls import path

from . import views

urlpatterns = [
    path("", views.opening, name="home"),
    path("cyberpolygon/", views.cyberpolygon, name="cyberpolygon"),
    path("cyberpolygon/category/<slug:category_slug>", views.show_category, name="category"),
    path("cyberpolygon/task/<slug:task_slug>", views.show_task, name="task"),
]
