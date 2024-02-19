# candidates/models.py
import os

from django.contrib.auth.models import User, AbstractUser, Group, Permission
from django.db import models
from django.utils.deconstruct import deconstructible


@deconstructible
class GenerateProfileImagePath(object):
    def __init__(self):
        pass

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        path = 'media/candidates/profile_pictures'
        name = f'profile_pictures/{ext}'
        return os.path.join(path, name)

user_profile_image_path = GenerateProfileImagePath()


class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to=user_profile_image_path, blank=True, null=True)
    # cv = models.FileField(upload_to='cv/', null=True, blank=True)

    # class Meta:
    #     # Add the 'auth' app label to avoid conflicts with the User model
    #     app_label = 'auth'
    #
    # # Specify unique related names for the groups and user_permissions fields
    # groups = models.ManyToManyField(Group, related_name='candidate_users')
    # user_permissions = models.ManyToManyField(Permission, related_name='candidate_users')
