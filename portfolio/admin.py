from django.contrib import admin
from .models import Project, ProjectImage, ContactMessage
from .models import CVDownload

import json
from django.urls import path
from django.shortcuts import render
from django.db.models import Count

from django.contrib import admin
from .models import SkillCategory, Skill, AboutMe
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin



from django.contrib import admin
from .models import Experience, Education
from adminsortable2.admin import SortableAdminMixin



# Inline for skills inside a category
class SkillInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Skill
    extra = 1  # Number of empty skill slots to show
    fields = ('name', 'proficiency', 'order')
    sortable_field_name = "order"

# Admin for SkillCategory with inline skills
@admin.register(SkillCategory)
class SkillCategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'order')
    inlines = [SkillInline]
    sortable_by = ('order',)

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'location', 'availability', 'email')





class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'tech_stack', 'order')
    list_editable = ('order',)
    inlines = [ProjectImageInline]

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')


@admin.register(CVDownload)
class CVDownloadAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'ip_address', 'browser', 'os', 'referrer')
    list_filter = ('timestamp', 'browser', 'os')
    search_fields = ('ip_address', 'user_agent', 'browser', 'os', 'referrer')
    readonly_fields = ('timestamp', 'ip_address', 'user_agent', 'browser', 'os', 'referrer')

    # Disable add/edit/delete in admin (optional)
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


       # Custom admin URLs
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('dashboard/', self.admin_site.admin_view(self.dashboard_view), name='cvdownload_dashboard'),
        ]
        return custom_urls + urls


    def dashboard_view(self, request):
            
            
            from django.db.models import Count

            # Downloads per day
            downloads_by_day = CVDownload.objects.extra({'day': "date(timestamp)"}).values('day').annotate(count=Count('id')).order_by('day')
            labels_day = [str(d['day']) for d in downloads_by_day]
            data_day = [d['count'] for d in downloads_by_day]

            # Downloads by browser
            downloads_by_browser = CVDownload.objects.values('browser').annotate(count=Count('id')).order_by('-count')
            labels_browser = [d['browser'] if d['browser'] else 'Unknown' for d in downloads_by_browser]
            data_browser = [d['count'] for d in downloads_by_browser]

            # Downloads by OS
            downloads_by_os = CVDownload.objects.values('os').annotate(count=Count('id')).order_by('-count')
            labels_os = [d['os'] if d['os'] else 'Unknown' for d in downloads_by_os]
            data_os = [d['count'] for d in downloads_by_os]

            context = dict(
                self.admin_site.each_context(request),
                labels_day=json.dumps(labels_day),
                data_day=json.dumps(data_day),
                labels_browser=json.dumps(labels_browser),
                data_browser=json.dumps(data_browser),
                labels_os=json.dumps(labels_os),
                data_os=json.dumps(data_os),
            )
            return render(request, 'admin/cvdownload_dashboard.html', context)







@admin.register(Experience)
class ExperienceAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('role', 'company', 'start_date', 'end_date')
    sortable_by = ('order',)

@admin.register(Education)
class EducationAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('degree', 'institution', 'start_date', 'end_date')
    sortable_by = ('order',)
