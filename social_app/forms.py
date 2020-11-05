from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from events.models import Profile, Category

choices = Category.objects.all().values_list('name', 'name')
choice_list = []
for item in choices:
    choice_list.append(item)

class EditProfileForm(UserChangeForm):
    username=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=('username', 'first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    bio=forms.CharField(max_length=500, widget=forms.Textarea(attrs={'class':'form-control'}))
    age=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    location=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    """categories = forms.MultipleChoiceField(required = False,
        widget=forms.CheckboxSelectMultiple,
        choices=choice_list,
    )"""
    class Meta:
        model=Profile
        fields = ('bio', 'age', 'location', 'categories')