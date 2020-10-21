import json
from django.contrib import admin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
from .models import Event


class EventAdmin(admin.ModelAdmin): 
    formfield_overrides = {
        map_fields.AddressField: {
          'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap','data-autocomplete-options': json.dumps({ 'types': ['geocode','establishment'], 'componentRestrictions': {
                  'country': 'us'
              }
          })}
          )
      }
    }
    list_display = ('title_text', 'location_text','date','time','category_text','description_text','address','geolocation')

    
# Register your models here.
admin.site.register(Event,EventAdmin)