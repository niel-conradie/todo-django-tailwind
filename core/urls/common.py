# https://docs.djangoproject.com/en/4.2/topics/http/urls/

from django.contrib import admin
from django.urls import path, include


DJANGO_URLS = [
    path("admin/", admin.site.urls),
]

LOCAL_URLS = [
    path("", include("pages.urls.urls", namespace="pages")),
    path("accounts/", include("accounts.urls.urls", namespace="accounts")),
]
