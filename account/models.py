# Create your models here.

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    mobile = models.CharField(max_length=15, null=True, blank=True)
    alternate_mobile = models.CharField(max_length=15, null=True, blank=True)

    ROLE_CHOICES = [
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
        ('firmadmin', 'FirmAdmin'),
        ("agent", 'Agent'),
    ]
    role = models.CharField(max_length=32, choices=ROLE_CHOICES, default='buyer',
        help_text="available choices -> buyer, seller, firmadmin, agent"                  
    )
    
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",  # Custom related name
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permission_set",  # Custom related name
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

