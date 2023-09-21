from .common import *


THIRD_PARTY_URLS = [
    path("__debug__/", include("debug_toolbar.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
]

urlpatterns = DJANGO_URLS + THIRD_PARTY_URLS + LOCAL_URLS
