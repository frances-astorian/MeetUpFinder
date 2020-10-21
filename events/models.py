# *  Author: N/A
# *  Date: N/A
# *  Code version: N/A
# *  URL: http://www.learningaboutelectronics.com/Articles/How-to-save-data-from-a-form-to-a-database-table-in-Django.php
# *  Software License: N/A
# *  Comment: Used for help writing events model

from django.db import models
from django.urls import reverse
from django_google_maps import fields as map_fields
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
    title_text = models.CharField("Event Name", max_length=50)
    location_text = models.CharField("Location", max_length=100)
    date = models.DateField(default=datetime.date.today)
    #time_text = models.CharField("Time", max_length=20)
    time = models.TimeField(default = '14:30')
    category_text = models.CharField("Category", max_length=50,
        choices = CATEGORY_CHOICES,
        default = '1')
    description_text = models.CharField("Description", max_length=200)
    address = map_fields.AddressField("Address", max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)
    def __str__(self):
        return self.title_text
    """"
    def get_absolute_url(self):
        return reverse('events:detail', kwargs={'pk': self.pk})    
    """