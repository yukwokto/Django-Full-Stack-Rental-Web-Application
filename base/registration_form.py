from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, RealtorProfile
from django.core.validators import RegexValidator


class UserForm(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        validators=[RegexValidator(r'^(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z\d]+$',
            'Username must contain at least one letter and one number, and only contain letters and numbers.')],
        error_messages={
            'required': 'Please enter a username.',
            'invalid': 'Username must contain at least one letter and one number, and only contain letters and numbers.',
        }
    )
    
    # to override the help text in form
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm your password'
        
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'bio', 'phone_number']
        
class RealtorProfileForm(forms.ModelForm):
    class Meta:
        model =  RealtorProfile
        fields = ['avatar', 'bio', 'phone_number', 'company']
        
        