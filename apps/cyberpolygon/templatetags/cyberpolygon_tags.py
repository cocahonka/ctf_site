from django import template

from apps.cyberpolygon.models import *

register = template.Library()

# * Replaced by decorators kwargs
# @register.simple_tag()
# def get_categories(user: User):
#     profile = Profile.objects.get(user=user)
#     return profile.category.all()


@register.inclusion_tag("cyberpolygon/list_categories.html")
def show_categories(categories, category_slug):
    return {
        "categories": categories,
        "category_slug": category_slug,
    }


@register.inclusion_tag("cyberpolygon/list_tasks.html")
def show_tasks(categories, category):
    # show all tasks
    if not category:
        tasks = Task.objects.filter(category__in=categories, is_published=True)
        return {"tasks": tasks}
    else:
        tasks = Task.objects.filter(category=category, is_published=True)
        return {"tasks": tasks}
