from django.urls import path

from . import views

app_name = 'events'

urlpatterns = [
    path('', views.EventsView.as_view(), name='index'),
    path('list/', views.EventsView.as_view(), name='event_list'),
    path('list/search/', views.search, name='search'),
    path('post/', views.postEventForm, name='post_event'),
    #path('post/', views.EventFormView.as_view(), name='post_event'),
    path('post/success/', views.event_success, name='event_success'),
    path('<int:pk>/', views.DetailView.as_view(), name = 'detail'),
    path('category/<str:cats>/', views.CategoryView, name='category'),
    path('category-list/', views.CategoryListView, name='category-list'),
    path('your-events/', views.YourEvents, name='your_events'),
    ]
