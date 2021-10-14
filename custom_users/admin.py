"""Custom User Admin
"""
from django.contrib import admin

from custom_users.models import CustomUser

# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    """Custom User Admin
    """

    fields = ('username', 'first_name', 'last_name', 'employee', 'restaurant')

admin.site.register(CustomUser, CustomUserAdmin)
