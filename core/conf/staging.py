from .common import *


## Deployment Security
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# https://docs.djangoproject.com/en/4.2/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["*"]


## Application definition
# https://docs.djangoproject.com/en/4.2/ref/settings/#installed-apps
STAGING_APPS = []

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS + STAGING_APPS

# https://docs.djangoproject.com/en/4.2/ref/settings/#middleware
STAGING_MIDDLEWARE = []

MIDDLEWARE = (
    DJANGO_MIDDLEWARE + THIRD_PARTY_MIDDLEWARE + LOCAL_MIDDLEWARE + STAGING_MIDDLEWARE
)


# https://docs.djangoproject.com/en/4.2/ref/settings/#root-urlconf
ROOT_URLCONF = "core.urls.staging"


## Email Backend
# https://docs.djangoproject.com/en/4.2/ref/settings/#email-backend
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
