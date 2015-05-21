"""
Definition of models.
"""
from django.db import models
from django.db.models import Sum



class ServiceLocation(models.Model):
    continent = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    area = models.CharField(max_length=200) 
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        """Returns a string representation of a poll."""
        return self.area

class ServiceLanguage(models.Model):
    language_code = models.CharField(max_length=50)
    language_name = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        """Returns a string representation of a poll."""
        return self.language_name

class PaymentTerm(models.Model):
    paymentterm = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        """Returns a string representation of a poll."""
        return self.paymentterm


# Create your models here.
class Tourguide(models.Model):
    """A poll object for use in the application views and repository."""
    username = models.CharField(max_length=200)
    useremail= models.CharField(max_length=200)
    isActive = models.BooleanField(default=True)
    servicelocation = models.ForeignKey(ServiceLocation)
    yearsOfExperience = models.IntegerField(default=0)
    gender = models.CharField(max_length=200)
    birthday = models.DateTimeField('birthday')
    Language = models.ForeignKey(ServiceLanguage)
    paymentterm = models.ForeignKey(PaymentTerm)
    profile = models.CharField(max_length=500)
    servicedetail = models.CharField(max_length=500)
    transportation = models.CharField(max_length=500)
    tourinterests = models.CharField(max_length=500)
    picture = models.BinaryField()
    license = models.CharField(max_length=500)
    licensepicture =models.BinaryField()

    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        """Returns a string representation of a poll."""
        return self.name

