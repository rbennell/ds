from django.contrib import admin
from .models import Building, Reading


# Register your models here.
@admin.register(Building)
class BuildingsAdmin(admin.ModelAdmin):
    pass


# Register your models here.
@admin.register(Reading)
class ReadingsAdmin(admin.ModelAdmin):
    pass
