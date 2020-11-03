# *  Author: N/A
# *  Date: N/A
# *  Code version: N/A
# *  URL: http://www.learningaboutelectronics.com/Articles/How-to-save-data-from-a-form-to-a-database-table-in-Django.php
# *  Software License: N/A
# *  Comment: Used for help writing events model

from django.db import models
from django.urls import reverse
from django_google_maps import fields as map_fields
from places.fields import PlacesField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from multiselectfield import MultiSelectField

import datetime

CATEGORY_CHOICES = (
    ('1', 'Food'),
    ('2', 'Career'),
    ('3', 'Physical Activity'),
    ('4', 'Civic Engagement'),
    ('5', 'Other'),

)
# Create your models here.
class Event(models.Model):
    title_text = models.CharField("Event Name", max_length=255)
    location_text = models.CharField("Location", max_length=100)
    date = models.DateField(default=datetime.date.today)
    #time_text = models.CharField("Time", max_length=20)
    time = models.TimeField(default = '14:30',help_text="Enter in 24 hour format (eg - 2:45 or 16:45)")
    category_text = models.CharField("Category", max_length=255,default = 'Uncategorized')
    description_text = models.CharField("Description", max_length=200)
    # address = map_fields.AddressField("Address", max_length=200)
    # geolocation = map_fields.GeoLocationField(max_length=100)
    organizer = models.ForeignKey(User, default = 1, on_delete=models.CASCADE)
    location=PlacesField()
    def __str__(self):
        return self.title_text
    """"
    def get_absolute_url(self):
        return reverse('events:detail', kwargs={'pk': self.pk})    
    """

class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Profile(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    categories = models.CharField("Category", max_length=50,
        choices = CATEGORY_CHOICES,
        default = '1')
    #profile_pic=models.ImageField(null=True, blank=True, upload_to='images/profile/')
    location = models.CharField("Location", null=True,max_length=100)
    age = models.IntegerField(null=True)
    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()