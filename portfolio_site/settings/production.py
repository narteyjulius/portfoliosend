from .base import *
import os
from pathlib import Path


print("this is prodution settings")


print("Loading production settings...")
print("BASE_DIR:", BASE_DIR)
print("ROOT_URLCONF:", ROOT_URLCONF)


if not SECRET_KEY:
    raise Exception("SECRET_KEY environment variable is required for production")

DEBUG = False

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'productiondb.sqlite3',
    }
}


# # Production database (PostgreSQL recommended)
# if os.getenv("DB_ENGINE") == "postgres":
#     DATABASES = {
#         "default": {
#             "ENGINE": "django.db.backends.postgresql",
#             "NAME": os.getenv("DB_NAME"),
#             "USER": os.getenv("DB_USER"),
#             "PASSWORD": os.getenv("DB_PASSWORD"),
#             "HOST": os.getenv("DB_HOST"),
#             "PORT": os.getenv("DB_PORT", "5432"),
#         },
#         "skills_db": {
#             "ENGINE": "django.db.backends.postgresql",
#             "NAME": os.getenv("SKILLS_DB_NAME"),
#             "USER": os.getenv("SKILLS_DB_USER"),
#             "PASSWORD": os.getenv("SKILLS_DB_PASSWORD"),
#             "HOST": os.getenv("SKILLS_DB_HOST"),
#             "PORT": os.getenv("SKILLS_DB_PORT", "5432"),
#         },
#     }
