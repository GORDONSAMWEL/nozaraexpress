from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Keep email unique
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

    USERNAME_FIELD = 'email'  # Login will still be by email
    REQUIRED_FIELDS = ['username']  # Username is required for registration

    objects = CustomUserManager()

    def __str__(self):
        return self.email
