from django.contrib import admin

from app.models import DayModel


class DayAdmin(admin.ModelAdmin):
    list_display = [
        "title",
    ]

    prepopulated_fields = {
        "slug": ("title",),
    }


admin.site.register(DayModel, DayAdmin)
