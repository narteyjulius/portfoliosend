# #!/usr/bin/env python
# """Django's command-line utility for administrative tasks."""
# import os
# import sys


# def main():
#     """Run administrative tasks."""
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
#     try:
#         from django.core.management import execute_from_command_line
#     except ImportError as exc:
#         raise ImportError(
#             "Couldn't import Django. Are you sure it's installed and "
#             "available on your PYTHONPATH environment variable? Did you "
#             "forget to activate a virtual environment?"
#         ) from exc
#     execute_from_command_line(sys.argv)


# if __name__ == '__main__':
#     main()



#!/usr/bin/env python
# import os
# import sys

# def main():
#     """Run administrative tasks."""
    
#     # Auto-detect environment (development by default)
#     # DJANGO_ENV = os.getenv("DJANGO_ENV", "development").lower()
#     DJANGO_ENV = os.getenv("DJANGO_ENV")
#     print('this is manage.py',DJANGO_ENV)

#     if DJANGO_ENV == "production":
#         os.environ.setdefault(
#             "DJANGO_SETTINGS_MODULE",
#             "portfolio_site.settings.production"
#         )
#     else:
#         os.environ.setdefault(
#             "DJANGO_SETTINGS_MODULE",
#             "portfolio_site.settings"  # base development settings
#         )

#     try:
#         from django.core.management import execute_from_command_line
#     except ImportError as exc:
#         raise ImportError(
#             "Couldn't import Django. Make sure it's installed "
#             "and your virtual environment is activated."
#         ) from exc
#     execute_from_command_line(sys.argv)


# if __name__ == "__main__":
#     main()





#!/usr/bin/env python
# import os
# import sys

# def main():
#     """Run administrative tasks."""

#     # Read env variable OR default to development
#     # env = os.environ.get("DJANGO_ENV", "development").lower()
#     env = os.environ.get("DJANGO_ENV")
    
#     # env = 'production'

#     if env == "production":
#         settings_module = "portfolio_site.settings.production"
#     else:
#         settings_module = "portfolio_site.settings.development"

#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

#     from django.core.management import execute_from_command_line
#     execute_from_command_line(sys.argv)


# if __name__ == "__main__":
#     main()



#!/usr/bin/env python
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

def main():
    """
    Auto-detect environment and load corresponding settings + .env file.
    Defaults to development if DJANGO_ENV is not set.
    """
    # Detect environment
    DJANGO_ENV = os.environ.get("DJANGO_ENV", "development").lower()

    #  Load correct .env file
    env_file = Path(__file__).parent / f".env.{DJANGO_ENV}"
    if env_file.exists():
        load_dotenv(dotenv_path=env_file)
        print(f"[INFO] Loaded environment file: {env_file}")
    else:
        print(f"[WARNING] {env_file} not found. Using defaults / system env variables.")

    #  Set Django settings module
    settings_module = {
        "development": "portfolio_site.settings.development",
        "production": "portfolio_site.settings.production",
    }.get(DJANGO_ENV, "portfolio_site.settings.development")

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)
    print(f"[INFO] Django is using settings module: {settings_module}")
    print(f"[INFO] DJANGO_ENV = {DJANGO_ENV}")

    #  Run Django command
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Make sure it's installed "
            "and your virtual environment is activated."
        ) from exc

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
