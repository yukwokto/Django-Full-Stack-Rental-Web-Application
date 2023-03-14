from django.forms import ModelForm, TextInput, DateInput
from .models import Rental

class RentalForm(ModelForm):
    class Meta:
        model = Rental
        labels = {
            'rent': 'Rent per month',
            'amenities': 'Amenities Included',
            'unit_iamge': 'Image'
        }
        fields = '__all__'
        exclude = ['landlord']
        widgets = {
            'rent': TextInput(attrs={'type': 'text'}),
            'availability': DateInput(attrs={'type': 'date'})
        }
        