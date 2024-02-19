from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Candidate

@receiver(post_save, sender=User)
def create_candidate(sender, instance, created, **kwargs):
    if created:
        Candidate.objects.create(user=instance)
