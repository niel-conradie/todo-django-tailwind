from django.contrib import admin

from todo.models import TaskModel


class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "day",
        "status",
        "created_at",
    ]

    list_filter = [
        "day",
        "status",
    ]

    search_fields = [
        "title",
    ]


admin.site.register(TaskModel, TaskAdmin)
