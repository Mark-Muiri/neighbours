from .models import Business, Neighbourhood, User
from django.forms import ModelForm
from django import forms

class AddBusinessForm(ModelForm):
    class Meta:
        model = Business
        exclude = ['profile', 'pubdate',]

class EditUserForm(ModelForm):
    class Meta:
        model = User
        exclude = ['user']

class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ['admin', 'occupants']

