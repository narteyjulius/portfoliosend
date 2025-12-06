# """
# WSGI config for portfolio_site project.

# It exposes the WSGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
# """

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')

# application = get_wsgi_application()




import os
from pathlib import Path
from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application

# Determine environment
DJANGO_ENV = os.environ.get("DJANGO_ENV", "development").lower()

# Load .env file if it exists
env_file = Path(__file__).resolve().parent.parent / f".env.{DJANGO_ENV}"
if env_file.exists():
    load_dotenv(dotenv_path=env_file)
    print(f"[INFO] Loaded environment file: {env_file}")
else:
    print(f"[WARNING] {env_file} not found. Using system environment variables.")

# Map DJANGO_ENV to the correct settings module
settings_module = {
    "development": "portfolio_site.settings.development",
    "production": "portfolio_site.settings.production",
}.get(DJANGO_ENV, "portfolio_site.settings.development")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

print(f"[INFO] Django WSGI using settings module: {settings_module}")

application = get_wsgi_application()
