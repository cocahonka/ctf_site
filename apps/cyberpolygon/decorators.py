from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404

from .models import Task


# Return in kwargs
# - original slug
# - categories
# - category or task (depend on input slug)
def categories_match_required(view_func):
    def wrap(request, *args, **kwargs):
        user_categories = request.user.profile.category.all()
        category_slug = kwargs.get("category_slug")
        task_slug = kwargs.get("task_slug")

        if category_slug:
            category = get_object_or_404(user_categories, slug=category_slug)
            return view_func(
                    request,
                    *args,
                    **dict(
                        kwargs,
                        category=category,
                        categories=user_categories,
                    )
                )

        if task_slug:
            task = get_object_or_404(Task, slug=task_slug)
            category_slug = task.category.slug

            if user_categories.filter(slug=category_slug).exists():
                return view_func(
                    request,
                    *args,
                    **dict(
                        kwargs,
                        task=task,
                        categories=user_categories,
                    )
                )
            else:
                raise Http404()

        raise Http404()

    return wrap
