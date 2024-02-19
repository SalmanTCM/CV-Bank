from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Candidate

@receiver(post_save, sender=User)
def create_candidate(sender, instance, created, **kwargs):
    if created:
        Candidate.objects.create(user=instance)

####### Auto Genarate Username #########


# @receiver(pre_save, sender=User)
# def set_username(sender, instance, **kwargs):
#     if not instance.username:
#         instance.username =f"{instance.first_name} {instance.last_name}".lower()
#         counter =1
#         while User.objects.filter(username=username):
#             username =f"{instance.first_name} {instance.last_name}_{counter}".lower()
#             counter +=1
#         instance.username = username


