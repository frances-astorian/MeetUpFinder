

from django.urls import path, include
from . import views
from .views import UserEditView, PasswordsChangeView, ProfileView
from django.contrib.auth import views as auth_views

app_name = 'social_app'

urlpatterns = [
    path('edit_profile/', views.UserEditView.as_view(), name = 'edit_profile'),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='social_app/change-password.html')),
    path('password/', PasswordsChangeView.as_view(template_name='social_app/change-password.html')),
    path('password_success/', views.password_success, name='password_success'),
    path('<int:pk>/profile/', views.ProfileView.as_view(), name='profile_page'),
    ]