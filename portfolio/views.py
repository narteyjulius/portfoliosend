import os
from django.http import FileResponse
from django.conf import settings
import httpagentparser
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings
from django.core.serializers import serialize
from .models import Project
from django.http import JsonResponse
from .models import CVDownload
from .models import CVDownload
from django.http import FileResponse
from user_agents import parse 
from .models import SkillCategory,AboutMe,Education,Experience



def home(request):
    projects = Project.objects.prefetch_related('images').all()
    # Prepare a dict mapping project id -> images list
    project_images = {}
    for project in projects:
        print(project)
        project_images[project.id] = [
            {'image': img.image.url, 'caption': img.caption} for img in project.images.all()
        ]

        print(project_images)
    # projects = Project.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # print(form)
        if form.is_valid():
            print('good')
            contact = form.save()
            send_mail(
                f"New message from {contact.name}",
                contact.message,
                # contact.email,
                # [settings.DEFAULT_FROM_EMAIL],
                # fail_silently=False,
                  from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
            )
            return render(request, "index.html", {"form": form, "projects": projects, "success": True})
    else:
        form = ContactForm()



    categories = SkillCategory.objects.prefetch_related('skills').all()
    about = AboutMe.objects.first()

    experiences = Experience.objects.all()
    educations = Education.objects.all()

    return render(request, "index.html", {"form": form, "projects": projects,  
                                          "project_images_json": project_images,
                                          'categories': categories,
                                          'about': about,
                                            'experiences': experiences,
                                            'educations': educations,
                                          })




def track_download(request):
    if request.method == "POST":
        CVDownload.objects.create()
        return JsonResponse({"status": "ok"})
    return JsonResponse({"error": "Invalid method"}, status=400)



def parse_user_agent(user_agent_string):
    """
    Returns the browser and OS name from a user agent string.
    """
    user_agent = parse(user_agent_string)
    browser = f"{user_agent.browser.family} {user_agent.browser.version_string}"
    os_name = f"{user_agent.os.family} {user_agent.os.version_string}"
    return browser, os_name

def get_client_ip(request):
    """
    Returns the client's IP address from the request object.
    Checks X-Forwarded-For first (if behind a proxy), then REMOTE_ADDR.
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        # X-Forwarded-For may contain multiple IPs; client IP is first
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR', '')
    return ip


def download_cv(request):
    file_path = os.path.join('static', 'cv/JuliusNarteyCV.pdf')
    
    # extract info
    ip = get_client_ip(request)
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    browser, os_name = parse_user_agent(user_agent)  # your function to parse UA

    # save to database
    CVDownload.objects.create(
        ip_address=ip,
        user_agent=user_agent,
        browser=browser,
        os=os_name,
    )

    # return file
    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='Julius_Nartey_CV.pdf')
