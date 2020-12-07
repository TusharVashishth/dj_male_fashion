from django.forms import ModelForm
from .models import UserAddress
from django import forms


class UserAddressForm(ModelForm):
    class Meta:
        model = UserAddress
        fields = ['user', 'street_address', 'apartment', 'city', 'state', 'pincode', 'phone_no']
        widgets = {
            'user': forms.HiddenInput()
        }
