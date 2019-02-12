from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Make User.email unique and required on db level
User._meta.get_field('email')._unique = True
User._meta.get_field('email').blank = False


class Profile(models.Model):
    '''
    Profile model extending built-in User model.
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Place additional fields here
    # e.g.
    location = models.CharField(max_length=50, blank=True)


@receiver(post_save, sender=User)
def user_post_save(sender, instance, created, **kwargs):
    if created:
        # When new User instance is created
        Profile.objects.create(user=instance)
    instance.profile.save()
