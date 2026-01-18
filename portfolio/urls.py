from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path("", views.home, name="home"),
      path("projects/<int:id>/", views.project_detail, name="project_detail"),
     path("track-download/", views.download_cv, name="download_cv"),
]
