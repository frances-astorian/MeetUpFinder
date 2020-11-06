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
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), required=True, widget=forms.CheckboxSelectMultiple)
    # friends = forms.ModelMultipleChoiceField(choices=Profile.get_friends(User), widget=forms.CheckboxSelectMultiple)
    # need to edit form so that it only displays current friends and not all
    class Meta:
        model=Profile
        fields = ('bio', 'age', 'location', 'categories','friends')
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        # add custom error messages
        self.fields['friends'].error_messages['required'] = 'Control Click to deselect existing friends'
    """def save(self, commit=True):
        instance = forms.ModelForm.save(self)
        instance.category_set.clear()
        instance.category_set.add(*self.cleaned_data['categories'])
        return instance"""
            