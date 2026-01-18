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
    
    
    summary = models.CharField(max_length=220, blank= True)
    problem = models.TextField( blank= True)
    solution = models.TextField( blank= True)
    challenges = models.TextField(blank=True)
    learnings = models.TextField(blank=True)

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
    




class SkillCategory(models.Model):
    name = models.CharField(max_length=100)  # e.g., Languages, Frameworks & Tools
    order = models.PositiveIntegerField(default=0)  # optional, for ordering

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(
        SkillCategory,
        related_name='skills',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)  # e.g., Python, Django, React
    proficiency = models.CharField(
        max_length=50,
        choices=[
            ('Beginner', 'Beginner'),
            ('Intermediate', 'Intermediate'),
            ('Advanced', 'Advanced'),
            ('Expert', 'Expert')
        ],
        blank=True,
        null=True
    )
    order = models.PositiveIntegerField(default=0)  # optional, for ordering within category

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} ({self.category.name})"



class AboutMe(models.Model):
    full_name = models.CharField(max_length=100, default="Julius Nartey")
    bio = models.TextField(
        default="I'm a software engineer experienced in building scalable " \
        "backend systems, developer-friendly APIs, and modern frontends." \
        " I enjoy solving hard problems and mentoring engineers."
    )
    location = models.CharField(max_length=100, default="Accra, Ghana")
    availability = models.CharField(max_length=100, default="Open to work / contract")
    email = models.EmailField(default="julius.nartey.71@gmail.com")
    profile_picture = models.ImageField(upload_to="profile_pics/", blank=True, null=True)

    class Meta:
        verbose_name = "About Me"
        verbose_name_plural = "About Me" # display on the selection page

    def __str__(self):
        return self.full_name



class Experience(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)  # null = current
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-start_date']

    def __str__(self):
        return f"{self.role} at {self.company}"


class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-start_date']

    def __str__(self):
        return f"{self.degree} at {self.institution}"
