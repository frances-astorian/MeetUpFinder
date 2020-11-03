# *  REFERENCES
# *  Title: How to Save Data from a Form to a Database Table in Django
# *  Author: N/A
# *  Date: N/A
# *  Code version: N/A
# *  URL: http://www.learningaboutelectronics.com/Articles/How-to-save-data-from-a-form-to-a-database-table-in-Django.php
# *  Software License: N/A
# *  Comment: Used for help writing EventForm class
from django import forms
from .models import Event
# from django_google_maps import widgets as map_widgets
# from django_google_maps import fields as map_fields
from places.fields import PlacesField

# from mapwidgets.widgets import GooglePointFieldWidget
import json
from datetime import date as currDate

CUSTOM_MAP = {
    "GooglePointFieldWidget": (
        ("zoom", 15),
        ("GooglePlaceAutocompleteOptions", {'componentRestrictions': {'country': 'us'}}),
    ),
}
class EventForm(forms.ModelForm):
    def clean_date(self):
            date=self.cleaned_data['date']
            if (date<currDate.today()):
                raise forms.ValidationError("Check the time and date to make sure event is not in the past!")
            return date
    class Meta:
        model=Event
        fields = ["title_text","location_text", "time", "date","category_text","description_text","location"]
        # fields = ["title_text", "location_text", "time", "date","category_text","description_text","address","location"]       
        # widgets = {
        #     # 'address':GoogleMapsAddressWidget(settings=CUSTOM_MAP),
        #     'address':map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap','data-autocomplete-options': json.dumps({ 'types': ['geocode','establishment'], 'componentRestrictions': {
        #           'country': 'us'
        #       }
        #   })}
        #   )
        # }
       
