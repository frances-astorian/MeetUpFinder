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


class EventForm(forms.ModelForm):
    class Meta:
        model=Event
        fields = ["title_text", "location_text", "time_text","category_text","description_text","address","geolocation"]