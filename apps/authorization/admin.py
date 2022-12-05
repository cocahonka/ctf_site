from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class ProfileAdmin(admin.ModelAdmin):
    fields = ("user", "is_verified", "category", "student_card", "get_html_student_card", "image", "get_html_image")
    list_display = ("user", "is_verified", "get_html_image")
    list_editable = ("is_verified",)
    readonly_fields = ("user", "get_html_student_card", "get_html_image")
    filter_horizontal = ("category",)

    def get_html_image(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50>")

    def get_html_student_card(self, object):
        if object.student_card:
            return mark_safe(f"<img src='{object.student_card.url}' width=150>")

    get_html_image.short_description = "Миниатюра аватарки"
    get_html_student_card.short_description = "Миниатюра студеческого"

    def get_categories(self, object):
        return "\n".join([str(category) for category in object.category.all()])


admin.site.register(Profile, ProfileAdmin)
