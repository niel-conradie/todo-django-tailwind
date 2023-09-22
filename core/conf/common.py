# https://docs.djangoproject.com/en/4.2/ref/settings/

from pathlib import Path

from environs import Env


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


## Environs
# https://pypi.org/project/environs/#usage-with-django
env = Env()
# Read .env into os.environ
env.read_env()


## Deployment Security
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# https://docs.djangoproject.com/en/4.2/ref/settings/#std:setting-SECRET_KEY
SECRET_KEY = env.str("DJANGO_SECRET_KEY")

# https://docs.djangoproject.com/en/4.2/ref/settings/#debug
DEBUG = env.bool("DJANGO_DEBUG", default=False)

# https://docs.djangoproject.com/en/4.2/ref/clickjacking/#clickjacking-prevention
SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)

# https://docs.djangoproject.com/en/4.2/ref/settings/#std:setting-SECURE_HSTS_SECONDS
SECURE_HSTS_SECONDS = env.int("DJANGO_SECURE_HSTS_SECONDS", default=2592000)  # 30 Days

# https://docs.djangoproject.com/en/4.2/ref/settings/#secure-hsts-include-subdomains
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool(
    "DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True
)

# https://docs.djangoproject.com/en/4.2/ref/settings/#secure-hsts-preload
SECURE_HSTS_PRELOAD = env.bool("DJANGO_SECURE_HSTS_PRELOAD", default=True)

# https://docs.djangoproject.com/en/4.2/ref/settings/#std:setting-SESSION_COOKIE_SECURE
SESSION_COOKIE_SECURE = env.bool("DJANGO_SESSION_COOKIE_SECURE", default=True)

# https://docs.djangoproject.com/en/4.2/ref/settings/#crsf-cookie-secure
CSRF_COOKIE_SECURE = env.bool("DJANGO_CSRF_COOKIE_SECURE", default=True)

# https://docs.djangoproject.com/en/4.2/ref/settings/#site-id
SITE_ID = 1


## Application definition
# https://docs.djangoproject.com/en/4.2/ref/settings/#installed-apps
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    "django.contrib.sites",
]

LOCAL_APPS = [
    "accounts.apps.AccountsConfig",
    "pages.apps.PagesConfig",
]

# https://docs.djangoproject.com/en/4.2/ref/settings/#middleware
DJANGO_MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # whitenoise requirement
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

LOCAL_MIDDLEWARE = []

# https://docs.djangoproject.com/en/4.2/ref/settings/#templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "core.context_processor.global_context.global_context",
            ],
        },
    },
]

# https://docs.djangoproject.com/en/4.2/ref/settings/#wsgi-application
WSGI_APPLICATION = "core.wsgi.wsgi.application"


## Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    "default": env.dj_db_url(
        "DATABASE_URL",
        default="postgres://postgres@db/postgres",
    )
}


## Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


## Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

# https://docs.djangoproject.com/en/4.2/ref/settings/#language-code
LANGUAGE_CODE = "en-us"

# https://docs.djangoproject.com/en/4.2/ref/settings/#time-zone
TIME_ZONE = "UTC"

# https://docs.djangoproject.com/en/4.2/ref/settings/#std:setting-USE_I18N
USE_I18N = True

# https://docs.djangoproject.com/en/4.2/ref/settings/#use-tz
USE_TZ = True


## Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# https://docs.djangoproject.com/en/4.2/ref/settings/#static-root
STATIC_ROOT = BASE_DIR / "staticfiles"

# https://docs.djangoproject.com/en/4.2/ref/settings/#static-url
STATIC_URL = "/static/"

# https://docs.djangoproject.com/en/4.2/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [BASE_DIR / "static"]

# http://whitenoise.evans.io/en/stable/django.html#add-compression-and-caching-support
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


## Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


## Custom User Model
# https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#substituting-a-custom-user-model
AUTH_USER_MODEL = "accounts.CustomUser"


## Authentication
LOGIN_URL = "accounts:login"
LOGIN_REDIRECT_URL = "pages:index"
LOGOUT_REDIRECT_URL = "pages:index"
