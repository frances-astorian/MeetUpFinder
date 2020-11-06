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
    categories = models.ManyToManyField(Category)
    friends = models.ManyToManyField(User, related_name='friends', blank = True)
    #profile_pic=models.ImageField(null=True, blank=True, upload_to='images/profile/')
    location = models.CharField("Location", null=True,max_length=100)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    age = models.IntegerField(null=True)
    
    def get_friends(self):
        return self.friends.all()
    
    def get_friends_no(self):
        return self.friends.all().count()
    
    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    

STATUS_CHOICES=(
    ('send','send'),
    ('accepted','accepted'),
    ('rejected','rejected'),
    ('deleted','deleted'),
)

class Relationship(models.Model):
    sender=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name= 'sender')
    receiver=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name= 'receiver')
    status=models.CharField(max_length=8,choices=STATUS_CHOICES)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"
    
@receiver(post_save, sender=Relationship)
def post_save_add_to_friends(sender, instance, created, **kwargs):
    sender_=instance.sender
    receiver_=instance.receiver
    if instance.status=='accepted':
        sender_.friends.add(receiver_.user)
        receiver_.friends.add(sender_.user)
        sender_.save()
        receiver_.save()

@receiver(post_save, sender=Relationship)
def post_save_delete_to_friends(sender, created, instance, **kwargs):
    sender_=instance.sender
    receiver_=instance.receiver
    if instance.status=='deleted':
        sender_.friends.remove(receiver_.user)
        receiver_.friends.remove(sender_.user)
        sender_.save()
        receiver_.save()
