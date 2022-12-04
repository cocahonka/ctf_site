from django.contrib import admin

from .models import *


class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "author", "complexity", "is_published")
    list_display_links = ("id", "title")
    search_fields = ("title", "content")
    list_editable = ("is_published",)
    list_filter = ("is_published", "category", "complexity", "author", "time_create")
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "id")
    list_display_links = ("name", "id")
    search_fields = ("name", "id")
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Task, TaskAdmin)
admin.site.register(Category, CategoryAdmin)
