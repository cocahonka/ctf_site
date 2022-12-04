from django.contrib import admin

from .models import *


class ProfileAdmin(admin.ModelAdmin):
    exclude = ["user"]
    filter_horizontal = ["category"]


admin.site.register(Profile, ProfileAdmin)
