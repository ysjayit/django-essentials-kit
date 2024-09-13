from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from .models import UserProfile


def user_profile(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        # assign to a group
        group = Group.objects.get(name='users')
        instance.groups.add(group)

        # create user profile
        UserProfile.objects.create(
            user=instance,
            name=instance.username,
            email=instance.email,
        )


post_save.connect(user_profile, sender=User)
