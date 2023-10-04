from django.contrib import admin

from app.models.terms import TermsModel


class TermsAdmin(admin.ModelAdmin):
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


admin.site.register(TermsModel, TermsAdmin)
