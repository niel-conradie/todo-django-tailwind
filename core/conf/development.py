import socket

from .common import *


## Deployment Security
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# https://docs.djangoproject.com/en/4.2/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]


## Application definition
# https://docs.djangoproject.com/en/4.2/ref/settings/#installed-apps
DEVELOPMENT_APPS = [
    "debug_toolbar",
    "django_browser_reload",
]

INSTALLED_APPS += DEVELOPMENT_APPS

# https://docs.djangoproject.com/en/4.2/ref/settings/#middleware
DEVELOPMENT_MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

MIDDLEWARE += DEVELOPMENT_MIDDLEWARE

# https://docs.djangoproject.com/en/4.2/ref/settings/#root-urlconf
ROOT_URLCONF = "core.urls.development"


## Email Backend
# https://docs.djangoproject.com/en/4.2/ref/settings/#email-backend
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


## django-debug-toolbar
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + [
    "127.0.0.1",
]
