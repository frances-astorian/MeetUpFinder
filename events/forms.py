# *  REFERENCES
# *  Title: How to save data from a form to a database in Django 
# *  Date: N/A
# *  Code version: N/A
# *  URL: http://www.learningaboutelectronics.com/Articles/How-to-save-data-from-a-form-to-a-database-table-in-Django.php
# *  Software License: N/A
# *  Comment: Used to help create the basic event form, when the event fields were all text fields

from django import forms
from .models import Event, Category
# from django_google_maps import widgets as map_widgets
# from django_google_maps import fields as map_fields
from places.fields import PlacesField
from django.contrib.auth.models import User


# from mapwidgets.widgets import GooglePointFieldWidget
import json
from datetime import date as currDate

choices = Category.objects.all().values_list('name', 'name')
choice_list = []
for item in choices:
    choice_list.append(item)

CUSTOM_MAP = {
    "GooglePointFieldWidget": (
        ("zoom", 15),
        ("GooglePlaceAutocompleteOptions", {'componentRestrictions': {'country': 'us'}}),
    ),
}
class EventForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        # access object through self.instance...
        self.fields['organizer'].queryset = User.objects.filter(id=user.id)
    def clean_date(self):
            date=self.cleaned_data['date']
            if (date<currDate.today()):
                raise forms.ValidationError("Check the time and date to make sure event is not in the past!")
            return date
    class Meta:
        model=Event
        fields = ["title_text","organizer","time", "date","category_text","description_text","location"]
        # fields = ["title_text", "location_text", "time", "date","category_text","description_text","address","location"]       
        # widgets = {
        #     # 'address':GoogleMapsAddressWidget(settings=CUSTOM_MAP),
        #     'address':map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap','data-autocomplete-options': json.dumps({ 'types': ['geocode','establishment'], 'componentRestrictions': {
        #           'country': 'us'
        #       }
        #   })}
        #   )
        # }
        widgets={
            'category_text':forms.Select(choices = choice_list, attrs={'class':'form-control', 'style': 'width:200px'})
        }
        
       
