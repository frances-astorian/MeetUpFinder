from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from django import forms
from django.shortcuts import render
from .forms import EditProfileForm, ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from events.models import Profile, Category, CATEGORY_CHOICES
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.db.models import Q
from events.models import Event




# Create your views here.

def is_valid_search(param):
    return param != '' and param is not None

class UsersView(generic.ListView):
    model = User
    template_name = 'social_app/search_users.html'
    # context_object_name = 'user_list'
    # result = User.objects.all()
    def get_context_data(self, **kwargs):
           context = super().get_context_data(**kwargs)  
           login_user_id = self.request.user.pk
           results=User.objects.exclude(id=login_user_id)
        #    for usersearch in results:
                # if is_valid_search(usersearch):
                #     results = results.filter(Q(first_name__icontains=usersearch)|Q(last_name__icontains=usersearch)|Q(username__icontains=usersearch))
           context["user_list"]=results
           return context
       


def search(request):
    userid=request.user.id
    userprofile=request.user.profile
    user = request.GET.get('user')
    results = User.objects.exclude(id=userid)
    template = 'social_app/search_users.html'
    # print(results)
    # context["friends"]=user.friends.all()
    if is_valid_search(user):
        results = results.filter(Q(first_name__icontains=user)|Q(last_name__icontains=user)|Q(username__icontains=user))

    context = {"user_list":results}
    return render(request, template, context)

def password_success(request):
    return render(request,'social_app/passwords_success.html')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'social_app/edit_profile.html'
    success_url = reverse_lazy('home') 

    def get_object(self):
        return self.request.user

def update_profile_success(request):
    return render(request,'social_app/profile_success.html')

def update_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            #profile_form.save_m2m()
            messages.success(request, ('Your profile was successfully updated!'))
            return HttpResponseRedirect('success/')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'social_app/edit_prefs.html', {
        'profile_form': profile_form
    })

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    sucess_url = reverse_lazy('home')

class ProfileView(generic.DetailView):
    model=Profile
    template_name='social_app/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        login_user_id = self.request.user.pk
        login_user_profile_id = self.request.user.profile.id
        users = Profile.objects.exclude(id=self.kwargs['pk'])
        context = super(ProfileView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        rsvp_event_list = Event.objects.filter(rsvps=login_user_id)
        context["page_user"]=page_user
        context['users']=users
        context['friends']=Profile.get_friends(page_user)
        context["cat_menu"]=cat_menu
        context["rsvp_event_list"] = rsvp_event_list
        return context
    
def change_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)
    user = User.objects.get(pk=request.user.id)
    if operation == 'add':
        friend.profile.friends.add(request.user)
        request.user.profile.friends.add(friend)
        # Profile.make_friend(request.user, friend)
    elif operation == 'remove':
        friend.profile.friends.remove(request.user)
        request.user.profile.friends.remove(friend)
        # Profile.lose_friend(request.user, friend)
    elif operation == 'add_search':
        friend.profile.friends.add(request.user)
        request.user.profile.friends.add(friend)
        # Profile.make_friend(request.user, friend)
        # return redirect('social_app:profile_page', pk=pk)
    elif operation == 'remove_search':
        friend.profile.friends.remove(request.user)
        request.user.profile.friends.remove(friend)
        # Profile.lose_friend(request.user, friend)
        # return redirect('social_app:profile_page', pk=pk)
    return redirect('social_app:search_users')