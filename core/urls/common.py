# https://docs.djangoproject.com/en/4.2/topics/http/urls/

from django.contrib import admin
from django.urls import path, include


DJANGO_URLS = [
    path("admin/", admin.site.urls),
]

THIRD_PARTY_URLS = [
    path("", include("allauth.urls")),
]

LOCAL_URLS = [
    path("", include("app.urls.urls")),
    path("", include("pages.urls.urls")),
]
