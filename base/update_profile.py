from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, RealtorProfile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'bio', 'phone_number']

class RealtorProfileForm(forms.ModelForm):
    class Meta:
        model = RealtorProfile
        fields = ['avatar', 'bio', 'phone_number', 'company']
