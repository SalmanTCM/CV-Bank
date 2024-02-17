from django.contrib import admin
from django.utils.html import format_html
from .models import CV
from django.http import HttpResponse
from django.urls import reverse

class CVAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'designation', 'experience', 'uploaded_at', 'resume')
    list_filter = ('uploaded_at', 'experience')
    search_fields = ('phone_number', 'designation', 'experience' )

    def view_pdf(self, obj):
        if obj.resume:
            return format_html('<a href="{}" target="_blank">View PDF</a>', reverse('view_pdf', args=[obj.id]))
        else:
            return "No PDF Available"
    view_pdf.short_description = 'Preview CV'

admin.site.register(CV, CVAdmin)
