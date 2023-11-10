from .common import *


DEVELOPMENT_URLS = [
    path("__debug__/", include("debug_toolbar.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
]

urlpatterns += DEVELOPMENT_URLS
