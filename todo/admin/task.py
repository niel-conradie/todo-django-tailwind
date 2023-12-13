from django.contrib import admin

from todo.models import TaskModel


class TaskAdmin(admin.ModelAdmin):
    """
    A Django admin class used to customize the admin interface for the TaskModel model.

    Parameters:
    - TaskAdmin (class): The base model admin that provides the basic user fields and methods.

    Fields:
    - list_display (list): The fields to be displayed in the list view.
    - list_filter (list): The fields to be used for filtering in the list view.
    - search_fields (list): The fields to be used for searching in the list view.
    """

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
