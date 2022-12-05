from django import template

from apps.authorization.models import Profile
from apps.cyberpolygon.models import *

register = template.Library()


@register.simple_tag()
def get_categories(user: User):
    profile = Profile.objects.get(user=user)
    return profile.category.all()


@register.inclusion_tag("cyberpolygon/list_categories.html")
def show_categories(categories, category_id):
    return {
        "categories": categories,
        "category_id": category_id,
    }


@register.inclusion_tag("cyberpolygon/list_tasks.html")
def show_tasks(categories, category_id):
    if category_id == 0:
        tasks = Task.objects.filter(category__in=categories, is_published=True)
        return {"tasks": tasks}
    else:
        tasks = Task.objects.filter(category_id=category_id, is_published=True)
        return {"tasks": tasks}
