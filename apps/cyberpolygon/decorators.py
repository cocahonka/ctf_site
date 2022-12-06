from django.http import Http404
from django.shortcuts import get_object_or_404, redirect

from .models import Task


def verified_required(view_func):
    def wrap(request, *args, **kwargs):
        if request.user.profile.is_verified:
            return view_func(request, *args, **kwargs)
        else:
            return redirect("cyberpolygon")

    return wrap


def categories_match_required(**filters):
    def decorator(view_func):
        def wrap(request, *args, **kwargs):
            user_categories = request.user.profile.category.all()
            category_slug = kwargs.get("category_slug")
            task_slug = kwargs.get("task_slug")

            if category_slug:
                category_filters = dict(filters.get("category_filters", []), slug=category_slug)
                category = get_object_or_404(user_categories, **category_filters)
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
                task_filters = dict(filters.get("task_filters", []), slug=task_slug)
                task = get_object_or_404(Task, **task_filters)
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

    return decorator
