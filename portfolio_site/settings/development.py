from .base import *
import os

DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
    "skills_db": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "skills.sqlite3",
    },
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

SECURE_SSL_REDIRECT = False


