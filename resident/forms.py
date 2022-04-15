from .models import Neighborhood, Profile
from django import forms
class HoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        exclude = ['admin']
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','neighborhood','bio','phone','profile_pic']
        
