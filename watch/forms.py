from .models import Business, Neighbourhood, User
from django.forms import ModelForm
from django import forms

class AddNeighbourhoodForm(ModelForm):
    class Meta:
        model = Project
        exclude = ['profile', 'pubdate',]

class EditUserForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ['admin', 'occupants']

