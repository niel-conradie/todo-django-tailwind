from django.contrib import admin

from app.models.privacy import PrivacyModel


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


admin.site.register(PrivacyModel, PrivacyAdmin)
