import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from dotenv import load_dotenv
# load_dotenv()
load_dotenv('.env')

User = get_user_model()





class Command(BaseCommand):
    help = "Create superuser from environment variables if none exists"

    def handle(self, *args, **kwargs):
        username = os.getenv("SUPERUSER_NAME")
        email = os.getenv("SUPERUSER_EMAIL")
        password = os.getenv("SUPERUSER_PASSWORD")
        
        print("DEBUG:", username, email, password)
        

        if not username or not email or not password:
            self.stdout.write(self.style.ERROR(
                "SUPERUSER_NAME, SUPERUSER_EMAIL, and SUPERUSER_PASSWORD must be set",
                
            ))
            return

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.SUCCESS("Superuser already exists"))
        else:
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' created"))
