"""
Customizations for the Django administration interface.
"""

from django.contrib import admin
from app.models import Tourguide, ServiceLocation

class LocationInline(admin.TabularInline):
    """Choice objects can be edited inline in the Poll editor."""
    model = ServiceLocation
    extra = 3

class TourGuideAdmin(admin.ModelAdmin):
    """Definition of the tourguide editor."""
    fieldsets = [
        (None, {'fields': ['username']}),
        (None, {'fields': ['useremail']}),
        (None, {'fields': ['username']}),
        (None, {'fields': ['username']}),
        (None, {'fields': ['yearsOfExperience']}),
        (None, {'fields': ['gender']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    #inlines = [ChoiceInline]
    list_display = ('username', 'yearsOfExperience', 'gender','pub_date')
    list_filter = ['pub_date']
    search_fields = ['name']
    date_hierarchy = 'pub_date'

class LocationAdmin(admin.ModelAdmin):
    """Definition of the ServiceLocation editor."""
    fieldsets = [
        (None, {'fields': ['continent']}),
        (None, {'fields': ['country']}),
        (None, {'fields': ['area']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    #inlines = [ChoiceInline]
    list_display = ('continent', 'country', 'area')
    list_filter = ['pub_date']
    search_fields = ['area']
    date_hierarchy = 'pub_date'


admin.site.register(Tourguide, TourGuideAdmin)
admin.site.register(ServiceLocation, LocationAdmin)
