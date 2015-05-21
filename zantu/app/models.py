"""
Definition of models.
"""
from django.db import models
from django.db.models import Sum

# Create your models here.
class Tourguide(models.Model):
    """A poll object for use in the application views and repository."""
    name = models.CharField(max_length=200)
    yearsOfExperience = models.IntegerField(default=0)
    gender =models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        """Returns a string representation of a poll."""
        return self.name


