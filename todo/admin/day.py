from django.contrib import admin

from todo.models import DayModel


class DayAdmin(admin.ModelAdmin):
    """
    A Django admin class used to customize the admin interface for the DayModel model.

    Parameters:
    - ModelAdmin (class): The base model admin that provides the basic user fields and methods.

    Fields:
    - list_display (list): The fields to be displayed in the list view.
    - prepopulated_fields (dict): The fields to be prepopulated based on other fields' values.
    """

    list_display = [
        "title",
    ]
    prepopulated_fields = {
        "slug": ("title",),
    }


admin.site.register(DayModel, DayAdmin)
