"""Restaurant Admin
"""
from django.contrib import admin

from restaurants.models import Menu

# Register your models here.

class MenuAdmin(admin.ModelAdmin):
    """Restaurant Model Admin
    """
    fields = ('name', 'restaurant', 'votes')

admin.site.register(Menu, MenuAdmin)
