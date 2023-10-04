from django.contrib import admin

from app.models.privacy import PrivacyModel


@admin.register(PrivacyModel)
class PrivacyAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "status",
        "modified",
    ]
    list_filter = [
        "status",
    ]
    search_fields = [
        "title",
    ]
