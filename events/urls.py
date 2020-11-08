from django.urls import path

from . import views

app_name = 'events'

urlpatterns = [
    path('', views.EventsView.as_view(), name='index'),
    path('list/', views.EventsView.as_view(), name='event_list'),
    path('list/search/', views.search, name='search'),
    #path('post/', views.postEventForm, name='post_event'),
    path('update/<int:pk>/', views.UpdateView.as_view(), name='update_event'),
    #path('update/<int:pk>/', views.updateEventForm, name='update_event'),
    path('post/', views.CreateEvent.as_view(), name='post_event'),
    path('post/success/', views.event_success, name='event_success'),
    path('update/<int:pk>/success/', views.update_success, name='update_success'),
    path('<int:pk>/', views.DetailView.as_view(), name = 'detail'),
    path('category/<str:cats>/', views.CategoryView, name='category'),
    path('category-list/', views.CategoryListView, name='category-list'),
    path('your-events/', views.YourEvents, name='your_events'),
    ]
