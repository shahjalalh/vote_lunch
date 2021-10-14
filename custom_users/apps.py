"""Custom User Apps
"""
from django.apps import AppConfig


class CustomUsersConfig(AppConfig):
    """Custom User App Config
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'custom_users'
