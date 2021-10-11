from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _

# Create your models here.
class CustomUser(AbstractUser):
    employee = models.BooleanField(verbose_name=_("Employee"), default=False)
    restaurant = models.BooleanField(verbose_name=_("Restaurant"), default=False) 
