from django.db import models
from django.utils.translation import gettext as _
from custom_users.models import CustomUser

# Create your models here.

class Menu(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=255)
    restaurant = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        verbose_name=_("Restaurant")
        )
    detail = models.TextField(verbose_name=_("Detail"), null=True, blank=True)
    price = models.DecimalField(
        verbose_name=_("Price"), 
        max_digits=19, 
        decimal_places=2
        )
    votes = models.IntegerField(verbose_name=_("Votes"), default=0)
    created_date = models.DateField(
        verbose_name='Created Date',
        auto_now_add=True
    )

    def __str__(self) -> str:
        return self.name
