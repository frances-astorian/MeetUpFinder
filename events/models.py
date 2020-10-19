# *  Author: N/A
# *  Date: N/A
# *  Code version: N/A
# *  URL: http://www.learningaboutelectronics.com/Articles/How-to-save-data-from-a-form-to-a-database-table-in-Django.php
# *  Software License: N/A
# *  Comment: Used for help writing events model

from django.db import models
from django.urls import reverse

# Create your models here.
class Event(models.Model):
    title_text = models.CharField(max_length=50)
    location_text = models.CharField(max_length=100)
    time_text = models.CharField(max_length=20)
    category_text = models.CharField(max_length=50)
    description_text = models.CharField(max_length=200)

    def __str__(self):
        return self.title_text
    """"
    def get_absolute_url(self):
        return reverse('events:detail', kwargs={'pk': self.pk})    
    """