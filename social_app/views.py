from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django import forms
from django.shortcuts import render
from .forms import EditProfileForm, ProfileForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from events.models import Profile
from django.shortcuts import get_object_or_404
from django.contrib import messages


# Create your views here.

def password_success(request):
    return render(request,'social_app/passwords_success.html')
"""
class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'social_app/edit_profile.html'
    success_url = reverse_lazy('home') 

    def get_object(self):
        return self.request.user
"""


def update_profile(request):
    if request.method == 'POST':
        user_form = EditProfileForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('home')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = EditProfileForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'social_app/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

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