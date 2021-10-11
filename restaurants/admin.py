from django.contrib import admin
from restaurants.models import Menu

# Register your models here.

class MenuAdmin(admin.ModelAdmin):
    pass

admin.site.register(Menu, MenuAdmin)
