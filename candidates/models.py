# candidates/models.py
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Candidate(AbstractUser):
    cv = models.FileField(upload_to='cv/', null=True, blank=True)

    class Meta:
        # Add the 'auth' app label to avoid conflicts with the User model
        app_label = 'auth'

    # Specify unique related names for the groups and user_permissions fields
    groups = models.ManyToManyField(Group, related_name='candidate_users')
    user_permissions = models.ManyToManyField(Permission, related_name='candidate_users')
