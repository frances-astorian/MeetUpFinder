import django_filters

from .models import Event

class eventFilter(django_filters.FilterSet):
    class Meta:
        model = Event
        fields = '__all__'
        exclude = ['PlacesField']