from .common import *


PRODUCTION_URLS = []

urlpatterns = DJANGO_URLS + THIRD_PARTY_URLS + LOCAL_URLS + PRODUCTION_URLS
