from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from accounts.forms import CustomUserCreationForm, CustomUserChangeForm


CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    """
    A Django admin class used to customize the admin interface for the CustomUser model.

    Parameters:
    - UserAdmin (class): The base user admin model that provides the basic user fields and methods.

    Fields:
    - add_form (class): The form to be used for adding users.
    - form (class): The form to be used for changing users.
    - model (class): The CustomUser model.
    - list_display (list): The fields to be displayed in the list view.
    - list_filter (list): The fields to be used for filtering in the list view.
    - ordering (list): The fields to be used for ordering the list view.
    - search_fields (list): The fields to be used for searching in the list view.
    """

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "is_active",
        "is_staff",
        "is_superuser",
    ]
    list_filter = [
        "is_active",
        "is_staff",
        "is_superuser",
    ]
    ordering = [
        "email",
    ]
    search_fields = [
        "username",
        "email",
    ]


admin.site.register(CustomUser, CustomUserAdmin)
