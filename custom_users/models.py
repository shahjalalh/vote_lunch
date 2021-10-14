"""Custom User Model"""
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class CustomUser(AbstractUser):
    """User extra fields
    """
    employee = models.BooleanField(verbose_name=_("Employee"), default=False)
    restaurant = models.BooleanField(
        verbose_name=_("Restaurant"),
        default=False
        )

    @property
    def full_name(self):
        """Full name property
        """
        return self.first_name + " " + self.last_name
