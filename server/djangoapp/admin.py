"""
Admin module for managing CarMake and CarModel in the Django admin interface.
"""

from django.contrib import admin
from .models import CarMake, CarModel

# Register your models here.

# CarModelInline class
class CarModelInline(admin.StackedInline):
    """
    Inline admin descriptor for CarModel objects.
    """
    model = CarModel
    extra = 5

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    """
    Admin view for CarModel.
    """
    fields = ['car_make', 'name', 'CAR_TYPES', 'type', 'year']

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    """
    Admin view for CarMake with inline CarModel.
    """
    fields = ['name', 'description']
    inlines = [CarModelInline]

# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
