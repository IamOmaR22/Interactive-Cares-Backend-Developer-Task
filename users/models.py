from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    # Set related_name for groups and user_permissions
    class Meta:
        db_table = 'auth_user'
        managed = False
        verbose_name_plural = 'users'

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )
