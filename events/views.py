# #***************************************************************************************
# *  REFERENCES
# *  Title: How to Save Data from a Form to a Database Table in Django
# *  Author: N/A
# *  Date: N/A
# *  Code version: N/A
# *  URL: http://www.learningaboutelectronics.com/Articles/How-to-save-data-from-a-form-to-a-database-table-in-Django.php
# *  Software License: N/A
# *  Comment: Used for help writing postEventForm method, which saves data from event forms
# ***************************************************************************************/
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .forms import EventForm
from .models import Event

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. This is for events.")

class EventsView(generic.ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events_list'

    def get_queryset(self):
        return Event.objects.all()



def postEventForm(request):
    form = EventForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, 'events/post_event.html', context)