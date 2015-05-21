"""
Customizations for the Django administration interface.
"""

from django.contrib import admin
from app.models import Tourguide


class TourGuideAdmin(admin.ModelAdmin):
    """Definition of the tourguide editor."""
    fieldsets = [
        (None, {'fields': ['name']}),
        (None, {'fields': ['yearsOfExperience']}),
        (None, {'fields': ['gender']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    #inlines = [ChoiceInline]
    list_display = ('name', 'yearsOfExperience', 'gender','pub_date')
    list_filter = ['pub_date']
    search_fields = ['name']
    date_hierarchy = 'pub_date'

admin.site.register(Tourguide, TourGuideAdmin)
