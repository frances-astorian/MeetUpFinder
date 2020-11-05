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
from django.db.models import Q
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.urls import reverse_lazy


from .forms import EventForm
from .models import Event, CATEGORY_CHOICES, Category
#from .filters import eventFilter

import datetime
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. This is for events.")

def event_success(request):
    return render(request,'events/event_success.html')

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'events/category_list.html', {'cat_menu_list':cat_menu_list})


class EventsView(generic.ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events_list'
    result = Event.objects.all()
    #ordering = ['-date']
    #myFilter = eventFilter()
    def get_queryset(self):
        result = Event.objects.exclude(date__lte=datetime.date.today())
        # query = self.request.GET.get('search')
        # if query:
        #     postresult = Event.objects.filter(title_text=query)
        #     result = postresult
        return result
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context=super(EventsView, self).get_context_data(*args, **kwargs)
        context["cat_menu"]=cat_menu
        return context

def CategoryView(request, cats):
    category_events = Event.objects.filter(category_text=cats)
    return render(request, 'events/categories.html', {'cats':cats, 'category_events':category_events})

# def EventsView(request):
#     model = Event
#     template_name = 'events/event_list.html'
#     events_list=Event.objects.all()
#     context_object_name = {'events_list' : events_list}
#     # lengthx=(Event.objects.all().count())
#     # if (request.method=='GET'):
#     #     {
#     #        search_query = request.GET.get('search', None);
#     #     }
#     return render(request,'events/event_list.html',{'events_list' : Event.objects.all()})


class DetailView(generic.DetailView):
    model = Event
    template_name = 'events/detail.html'
    #context_object_name = 'detail'
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context=super(DetailView, self).get_context_data(*args, **kwargs)
        context["cat_menu"]=cat_menu
        return context

"""
class EventFormView(FormView):
    template_name = 'events/post_event.html'
    form_class = EventForm
    success_url = reverse_lazy('event_success')
"""

def postEventForm(request):
    form = EventForm(user = request.user.id, data = request.POST or None)
    if form.is_valid():
        #form.instance.organizer = request.user
        
        # name = form.cleaned_data['title_text']
        # location = form.cleaned_data['location_text']
        # time = form.cleaned_data['time']
        # date=form.cleaned_data['date']
        # category = form.cleaned_data['category_text']
        # description = form.cleaned_data['description_text']
        # address1 = form.cleaned_data['address']
        # e = Event(title_text = name, location_text = location, 
        #    date=date, time = time, category_text = category, description_text = description, address = address1)
        
        form.save()
        return HttpResponseRedirect('success/')
    context = {'form': form}
    return render(request, 'events/post_event.html', context)

#new....for searching
# def get_query_set(request):
#     queryset = []
#     queries = query.split(" ")
#     for q in queries:
#         posts = Event.objects.filter(
#             Q(title__icontains=q)|
#             Q(body__icontains=q)
#         ).distinct()
#
#         for post in posts:
#             queryset.append(post)
#
#     return list(set(queryset))
def is_valid_search(param):
    return param != '' and param is not None

def search(request):
    template = 'events/event_list.html'

    results = Event.objects.all()

    title_contains = request.GET.get('title_contains')
    description_contains = request.GET.get('description_contains')
    location_contains = request.GET.get('location_contains')
    event_date = request.GET.get('event_date')
    event_time = request.GET.get('event_time')
    category = request.GET.get('category')


    if is_valid_search(title_contains):
        results = results.filter(Q(title_text__icontains=title_contains))

    if is_valid_search(description_contains):
        results = results.filter(Q(description_text__icontains=description_contains))

    if is_valid_search(location_contains):
        results = results.filter(Q(location_text__icontains=location_contains))

    if is_valid_search(event_date):
        results = results.filter(date=event_date)


    if is_valid_search(event_time):
        results = results.filter(time=event_time)

    if is_valid_search(category) and category != "Choose...":
        results = results.filter(category_text=category)

    results = results.exclude(date__lte=datetime.date.today())
    context = {"events_list": results}

    return render(request, template, context)

# def search(request):
#     template = 'events/event_list.html'
#
#     query = request.GET.get('q')
#     results = Event.objects.filter(Q(title_text__icontains=query) | Q(description_text__icontains=query)).exclude(date__lte=datetime.date.today())
#     context = {"events_list": results}
#     return render(request, template, context)