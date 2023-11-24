from django.contrib import admin

from todo.models import DayModel


class DayAdmin(admin.ModelAdmin):
    list_display = [
        "title",
    ]

    prepopulated_fields = {
        "slug": ("title",),
    }


admin.site.register(DayModel, DayAdmin)
