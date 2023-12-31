from django import forms
from .models import Room

class RoomCreationForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'slug']

class GroupCreationForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'users']