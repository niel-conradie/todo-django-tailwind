from django.contrib import admin

from app.models.privacy import Privacy


@admin.register(Privacy)
class CustomPrivacyAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
    )
