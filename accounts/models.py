from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import FileExtensionValidator
from django.conf import settings

class NewEmployee(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = ('admin', 'Admin')
        MANAGER = ('manager', 'Manager')
        EMPLOYEE = ('employee', 'Employee')
        
    role = models.CharField(max_length=100, choices=Role.choices)
    date_joined = models.DateTimeField(auto_now_add=True)

@receiver(post_save, sender=NewEmployee)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, _ = Profile.objects.get_or_create(user=instance)
        profile.role = instance.role # type: ignore
        profile.save()

@receiver(post_save, sender=NewEmployee)
def update_profile(sender, instance, **kwargs):
    try:
        profile = Profile.objects.get(user=instance)
        profile.role = instance.role
        profile.first_name = instance.first_name
        profile.last_name = instance.last_name
        profile.save()
    except Profile.DoesNotExist:
        pass
        
        
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, help_text='Enter your phone number', blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    full_name = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(max_length=200, blank=True, null=True)

    date_started = models.DateField(blank=True, null=True)
    def __str__(self):
        return self.user.username


    
