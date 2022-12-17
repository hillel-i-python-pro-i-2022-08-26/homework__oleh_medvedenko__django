from django.contrib import admin

from . import models


@admin.register(models.VisitHandler)
class PhoneBookAdmin(admin.ModelAdmin):
    list_display = ("user", "session_key", "path", "count_of_visits")
    search_fields = (
        "user",
        "session_key",
        "path",
    )
    list_filter = ("user",)
    list_per_page = 20
