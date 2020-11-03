from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django import forms
from django.shortcuts import render
from .forms import EditProfileForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from events.models import Profile
from django.shortcuts import get_object_or_404

# Create your views here.

def password_success(request):
    return render(request,'social_app/passwords_success.html')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'social_app/edit_profile.html'
    success_url = reverse_lazy('home') 

    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    sucess_url = reverse_lazy('home')

class ProfileView(generic.DetailView):
    model=Profile
    template_name='social_app/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ProfileView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"]=page_user
        return context