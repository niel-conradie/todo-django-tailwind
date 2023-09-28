from .common import *


STAGING_URLS = []

urlpatterns = DJANGO_URLS + THIRD_PARTY_URLS + LOCAL_URLS + STAGING_URLS
