# candidates/admin.py
from django.contrib import admin
from .models import Candidate

# Register the Candidate model with the admin site
admin.site.register(Candidate)
