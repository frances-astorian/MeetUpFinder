from django.urls import path

from . import views

app_name = 'events'

urlpatterns = [
    path('', views.EventsView.as_view(), name='index'),
    path('list/', views.EventsView.as_view(), name='event_list'),
    # path('list/', views.EventsView, name='event_list'),
    path('post/', views.postEventForm, name='post_event'),
    path('<int:pk>/', views.DetailView.as_view(), name = 'detail'),
    ]
