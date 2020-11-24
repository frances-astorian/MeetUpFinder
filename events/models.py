# *************************************************************************************************
# *  REFERENCES
# *  Title: How to save data from a form to a database in Django 
# *  Date: N/A
# *  Code version: N/A
# *  URL: http://www.learningaboutelectronics.com/Articles/How-to-save-data-from-a-form-to-a-database-table-in-Django.php
# *  Software License: N/A
# *  Comment: Used for help writing events model
# *  ---------------------------------------------------------------------------------------------
# *  Title: How to add user profile in Django
# *  Author: Vitor Frietas
# *  Date: N/A
# *  Code version: N/A
# *  URL: https://simpleisbetterthancomplex.com/tutorial/2016/11/23/how-to-add-user-profile-to-django-admin.html
# *  Software License: N/A
# *  Comment: Used for help writing profile model
# *  ---------------------------------------------------------------------------------------------
# *  Title: Django user profile 
# *  Author: N/A
# *  Date: N/A
# *  Code version: N/A
# *  URL: https://stackoverflow.com/questions/54943171/how-can-i-create-user-profile-after-registering-user-in-django-using-signals
# *  Software License: N/A
# *  Comment: Help with @reciever and @classmethod functions
# *  ---------------------------------------------------------------------------------------------
# *  Title: Create Blog Like Button - Django Blog #18
# *  Author: N/A
# *  Date: N/A(Date accessed : 11/11/2020)
# *  Code version: N/A
# *  URL: https://www.youtube.com/watch?v=PXqRPqDjDgc&ab_channel=Codemy.com
# *  Software License: BSD
# *  Note : Used to help create the RSVP feature for each event (in the Event model)

# *  Author: Max Goodridge
# *  Date: Mar 28, 2017
# *  Code version: N/A
# *  URL: https://www.youtube.com/watch?v=_DqmVMlJzqA
# *  Software License: N/A
# *  Comment: Used for help in writing the friends features and functions

# *  Author: Oscar Cortez
# *  Date: Apr 13, 2020
# *  Code version: Python 3
# *  URL: https://pypi.org/project/dj-places/
# *  Software License: BSD license
# *  Comment: Used for setting up the map feature along with geolocation, autofill in address bar.

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

STATUS_CHOICES=(
    ('send','send'),
    ('accepted','accepted'),
    ('rejected','rejected'),
    ('deleted','deleted'),
)

# Create your models here.
class Event(models.Model):
    title_text = models.CharField("Event Name", max_length=255)
    # location_text = models.CharField("Location", max_length=100)
    date = models.DateField(default=datetime.date.today)
    time = models.TimeField(default = '14:30',help_text="Enter in 24 hour format (eg - 2:45 or 16:45)")
    category_text = models.CharField("Category", max_length=255,default = 'Uncategorized')
    description_text = models.CharField("Description", max_length=200)
    organizer = models.ForeignKey(User, default = 1, on_delete=models.CASCADE,related_name='organizer')
    location=PlacesField()
    # rsvp= models.ManyToManyField(User, related_name='rsvp', blank=True )
    rsvps = models.ManyToManyField(User, related_name='rsvps') #blank=True )

    def rsvp_total(self):
        return self.rsvps.count()

    def rsvps_list(self):
        return self.rsvps
    def rsvps_list_all(self):
        return self.rsvps.all()
    
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
    categories = models.ManyToManyField(Category, blank=True)
    friends = models.ManyToManyField(User, related_name='friends', blank = True)
    current_user = models.ForeignKey(User, related_name='owner', null=True, on_delete=models.CASCADE)
    # rsvped=models.ManyToManyField(Event, related_name='rsvped', blank=True)
    #profile_pic=models.ImageField(null=True, blank=True, upload_to='images/profile/')
    location = models.CharField("Location", null=True,max_length=100)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    age = models.IntegerField(null=True)
    
    def get_categories(self):
        return self.categories.all()
    def get_categories_no(self):
        return self.categories.all().count()
    def get_friends(self):
        return self.friends.all()
    def get_friends_no(self):
        return self.friends.all().count()

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend = cls.objects.get(id=current_user.id)
        friendreq =cls.objects.get(id=new_friend.id)
        friend.friends.add(new_friend)
        friendreq.friends.add(current_user)

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend = cls.objects.get(id=current_user.id)
        friendreq =cls.objects.get(id=new_friend.id)
        friend.friends.remove(new_friend)
        friendreq.friends.remove(current_user)
            
    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# class Friend(models.Model):
#     users = models.ManyToManyField(User)
#     current_user = models.ForeignKey(User, related_name='owner', null=True)

#     @classmethod
#     def make_friend(cls, current_user, new_friend):
#         friend, created = cls.objects.get_or_create(
#             current_user=current_user
#         )
#         friend.users.add(new_friend)

#     @classmethod
#     def lose_friend(cls, current_user, new_friend):
#         friend, created = cls.objects.get_or_create(
#             current_user=current_user
#         )
#         friend.users.remove(new_friend)

# class Relationship(models.Model):
#     sender=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name= 'sender')
#     receiver=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name= 'receiver')
#     status=models.CharField(max_length=8,choices=STATUS_CHOICES)
#     updated=models.DateTimeField(auto_now=True)
#     created=models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return f"{self.sender}-{self.receiver}-{self.status}"
    
# @receiver(post_save, sender=Relationship)
# def post_save_add_to_friends(sender, instance, created, **kwargs):
#     sender_=instance.sender
#     receiver_=instance.receiver
#     if instance.status=='accepted':
#         sender_.friends.add(receiver_.user)
#         receiver_.friends.add(sender_.user)
#         sender_.save()
#         receiver_.save()

# @receiver(post_save, sender=Relationship)
# def post_save_delete_to_friends(sender, created, instance, **kwargs):
#     sender_=instance.sender
#     receiver_=instance.receiver
#     if instance.status=='deleted':
#         sender_.friends.remove(receiver_.user)
#         receiver_.friends.remove(sender_.user)
#         sender_.save()
#         receiver_.save()
        
# @receiver(post_save, sender=Relationship)
# def post_save_send_to_friends(sender, created, instance, **kwargs):
#     sender_=instance.sender
#     receiver_=instance.receiver
#     if instance.status=='send':
#         sender_.status='send'
#         receiver_.status='send'
#         sender_.save()
#         receiver_.save()
