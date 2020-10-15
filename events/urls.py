from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.EventsView.as_view(), name='event_list'),
    path('post/', views.postEventForm, name='post_event'),
]
