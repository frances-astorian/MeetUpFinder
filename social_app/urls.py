

from django.urls import path, include
from django.conf.urls import url
from . import views
#from .views import PasswordsChangeView, ProfileView
from .views import PasswordsChangeView, ProfileView, UserEditView 
from django.contrib.auth import views as auth_views

app_name = 'social_app'

urlpatterns = [
    path('edit_profile/', views.UserEditView.as_view(), name = 'edit_profile'),
    path('preferences/', views.update_profile, name = 'edit_prefs'),
    path('preferences/success/', views.update_profile_success, name = 'edit_success'),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='social_app/change-password.html')),
    path('password/', PasswordsChangeView.as_view(template_name='social_app/change-password.html')),
    path('password_success/', views.password_success, name='password_success'),
    path('<int:pk>/profile/', views.ProfileView.as_view(), name='profile_page'),
    path('search_users/', views.UsersView.as_view(), name='search_users'),
    path('search/', views.search, name='search'),
    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_friends, name='change_friends'),
    ]