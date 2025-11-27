from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"




class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=300, help_text="Comma-separated technologies")
    live_link = models.URLField(blank=True, null=True)
    repo_link = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0, help_text="Order in the portfolio")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='projects/')
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.project.title} - {self.caption or 'Image'}"
    



class CVDownload(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)
    browser = models.CharField(max_length=50, blank=True, null=True)
    os = models.CharField(max_length=50, blank=True, null=True)
    referrer = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return f"{self.ip_address} - {self.timestamp}"