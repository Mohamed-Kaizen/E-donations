"""Django base settings for E-donations project."""
import pathlib
from datetime import datetime, timedelta

from decouple import Csv, config
from dj_database_url import parse as db_url
from django.utils.translation import gettext_lazy as _

# General
# ------------------------------------------------------------------------------
BASE_DIR = pathlib.Path().absolute()

TEMPLATES_DIR = [BASE_DIR.joinpath("templates")]

# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = config("DEBUG", cast=bool)

ADMIN_URL = config("ADMIN_URL", cast=str, default="admin")

# using python-decouple to hide the SECRET_KEY
SECRET_KEY = config("SECRET_KEY")

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv(str))

SITE_ID = 1

# URLS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = "e_donations.urls"

# https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = "e_donations.wsgi.application"

# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "django.contrib.sites",
]
THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework.authtoken",
    "axes",
    "import_export",
    "corsheaders",
    "storages",
]

LOCAL_APPS = ["users.apps.UsersConfig", "donations.apps.DonationsConfig", "contact.apps.ContactConfig"]

# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIDDLEWARE
# ------------------------------------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",  # django-cors-headers
    "whitenoise.middleware.WhiteNoiseMiddleware",  # whitenoise
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "axes.middleware.AxesMiddleware",  # django-axes
]

# AUTHENTICATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#authentication-backends
AUTHENTICATION_BACKENDS = (
    "axes.backends.AxesBackend",
    "django.contrib.auth.backends.ModelBackend",
)

# https://docs.djangoproject.com/en/dev/ref/settings/#auth-user-model
AUTH_USER_MODEL = "users.CustomUser"

# https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = "/"

# https://docs.djangoproject.com/en/dev/ref/settings/#login-url
LOGIN_URL = "/"

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = [
# https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django  # noqa: B950
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",

]


# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"  # noqa: B950
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
    {
        "NAME": "pwned_passwords_django.validators.PwnedPasswordsValidator",
        "OPTIONS": {
            "error_message": "Oh no — pwned! This password has been seen "
            "%(amount)d times before",
            "help_message": "Your password can't be a commonly used password.",
        },
    },
]

# STATIC (CSS, JavaScript, Images)
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "/static/"

# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS  # noqa: B950
STATICFILES_DIRS = [BASE_DIR.joinpath("static")]

# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = BASE_DIR.joinpath("static_root")

# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = "/media/"

# https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = BASE_DIR.joinpath("media")

# Internationalization
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = "en-us"

# Local time zone. Choices are
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# though not all of them may be available with every OS.
# In Windows, this must be set to your system time zone.
TIME_ZONE = "Africa/Addis_Ababa"

# https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True

# https://docs.djangoproject.com/en/dev/ref/settings/#locale-paths
LOCALE_PATHS = [BASE_DIR.joinpath("local")]

LANGUAGES = (("en", _("English")), ("am", _("Amharic")))

# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND  # noqa: B950
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        "DIRS": TEMPLATES_DIR,
        "APP_DIRS": True,
        "OPTIONS": {
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
            "debug": DEBUG,
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors  # noqa: B950
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "users.context_processors.from_settings",
            ],
        },
    }
]

# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = True

# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = True

# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-secure
SESSION_COOKIE_SECURE = not DEBUG

# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-secure
CSRF_COOKIE_SECURE = not DEBUG

# https://docs.djangoproject.com/en/dev/ref/settings/#secure-ssl-redirect
SECURE_SSL_REDIRECT = not DEBUG


# Email
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
if DEBUG:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

else:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = config("EMAIL_USER", cast=str)
    EMAIL_HOST_PASSWORD = config("EMAIL_PASSWORD", cast=str)

# DATABASES
# ------------------------------------------------------------------------------
DATABASES = {
    "default": config("DATABASE_URL", cast=db_url, default="sqlite:///db.sqlite3")
}

# LOGGER
# ------------------------------------------------------------------------------
LOG_DATE_FORMAT = datetime.now().strftime("%B %d, %Y")
CONSOLE_LOGGING_FILE = BASE_DIR.joinpath(f"logs/django_{LOG_DATE_FORMAT}.log")

LOGGING = {
    "version": 1,
    "loggers": {
        # root logger
        "": {"level": "INFO", "handlers": ["console"]},
        "django": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
        "django.server": {"propagate": True},
    },
    "formatters": {
        "my_formatter": {
            "format": "{asctime} {levelname} {threadName} {name} {filename}"
            " {funcName} {module} {message}",
            "style": "{",
        },
    },
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
            "include_html": True,
        },
        "console": {"class": "logging.StreamHandler", "formatter": "my_formatter"},
    },
}

# Third-Party Settings
# djangorestframework
# ------------------------------------------------------------------------------
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.AllowAny",),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
}

# whitenoise
# ------------------------------------------------------------------------------
if DEBUG:
    INSTALLED_APPS.insert(0, "whitenoise.runserver_nostatic")

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# django-extensions
# ------------------------------------------------------------------------------
if DEBUG:
    INSTALLED_APPS.append("django_extensions")


# django-axes
# ------------------------------------------------------------------------------
AXES_COOLOFF_TIME = timedelta(minutes=60) if not DEBUG else timedelta(minutes=5)
AXES_FAILURE_LIMIT = 5
AXES_USE_USER_AGENT = True

# django-cors-headers
# ------------------------------------------------------------------------------
# https://github.com/adamchainz/django-cors-headers#cors_origin_allow_all
# Todo: Change this in production
CORS_ORIGIN_ALLOW_ALL = True

# django-storages
# ------------------------------------------------------------------------------
if not DEBUG:
    DEFAULT_FILE_STORAGE = "storages.backends.dropbox.DropBoxStorage"

    DROPBOX_OAUTH2_TOKEN = config("DROPBOX_OAUTH2_TOKEN", cast=str)

    DROPBOX_ROOT_PATH = "media"

# Your settings...
# ------------------------------------------------------------------------------

if DEBUG:

    ENVIRONMENT_NAME = _("Dev")

    ENVIRONMENT_COLOR = "red"

else:

    ENVIRONMENT_NAME = _("Production")

    ENVIRONMENT_COLOR = "green"

CUSTOM_RESERVED_NAMES = []
