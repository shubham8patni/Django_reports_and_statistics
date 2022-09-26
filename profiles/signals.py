from cProfile import Profile
from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender = User)

def post_save_create_profile(sender, instance, created, **kwargs):  # created is a boolean value True or False, it will only be recieved as True only and only when a user is created
    print(sender)
    print(created)
    print(instance)
    if created:
        Profile.objects.create(user=instance) 