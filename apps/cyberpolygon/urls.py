from django.urls import path

from . import views

urlpatterns = [
    path("", views.opening, name="home"),
    path("cyberpolygon/", views.cyberpolygon, name="cyberpolygon"),
    path("cyberpolygon/task/<int:task_id>", views.show_task, name="task"),
    path("cyberpolygon/category/<int:category_id>", views.show_category, name="category"),
]
