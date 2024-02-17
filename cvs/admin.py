from django.contrib import admin
from django.utils.html import format_html
from .models import CV
from django.http import HttpResponse
from django.urls import reverse

class CVAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'designation', 'experience', 'resume', 'resume_actions')
    list_filter = ('uploaded_at', 'experience')
    search_fields = ('phone_number', 'designation', 'experience', 'email', 'full_name')
    list_per_page = 10

    # def view_pdf(self, obj):
    #     if obj.resume:
    #         return format_html('<a href="{}" target="_blank">View PDF</a>', reverse('view_pdf', args=[obj.id]))
    #     else:
    #         return "No PDF Available"
    # view_pdf.short_description = 'Preview CV'

    def resume_actions(self, obj):
        if obj.resume:
            preview_link = format_html(
                '<a class="preview-button" href="{}" target="_blank"><i class="fas fa-eye"></i>view</a>',
                reverse('view_pdf', args=[obj.id])
            )
            download_link = format_html(
                '<a class="download-button" href="{}"><i class="fas fa-download"></i> Download</a>',
                reverse('download_pdf', args=[obj.id])
            )
            return format_html("{} {}", preview_link, download_link)
        else:
            return "No PDF Available"

    resume_actions.short_description = 'Actions'

    class Media:
        css = {
            'all': ('css/admin.css',)
        }
        js = ('https://kit.fontawesome.com/f2fe9a199b.js',)

admin.site.register(CV, CVAdmin)
