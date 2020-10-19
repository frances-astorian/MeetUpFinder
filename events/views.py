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
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views import generic
from django.shortcuts import get_object_or_404


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


class DetailView(generic.DetailView):
    model = Event
    template_name = 'events/detail.html'
    #context_object_name = 'detail'


def postEventForm(request):
    form = EventForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['title_text']
        location = form.cleaned_data['location_text']
        time = form.cleaned_data['time_text']
        category = form.cleaned_data['category_text']
        description = form.cleaned_data['description_text']
        e = Event(title_text = name, location_text = location, 
            time_text = time, category_text = category, description_text = description)
        e.save()
    context = {'form': form}
    return render(request, 'events/post_event.html', context)