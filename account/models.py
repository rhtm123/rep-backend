# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    mobile = models.CharField(max_length=15)
    ROLE_CHOICES = [
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
        ('admin', 'Admin'),
        ("agent", 'Agent'),
    ]
    role = models.CharField(max_length=6, choices=ROLE_CHOICES, default='buyer')
