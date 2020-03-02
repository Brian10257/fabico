from django import forms
from django.forms import ClearableFileInput
from .models import Career


class CareerForm(forms.ModelForm):
    class Meta:
        model = Career
        fields = ['name', 'email', 'phone_number', 'place_of_birth',
                  'current_city', 'neighbour_hood', 'current_employment', 'subject', 'message', 'file_upload', 'user_id']
        widgets = {
            'name': forms.TextInput(attrs={'size': 50}), 'email': forms.TextInput(attrs={'size': 50}), 'subject': forms.TextInput(attrs={'size': 50}), 'phone_number': forms.TextInput(attrs={'size': 50}), 'place_of_birth': forms.TextInput(attrs={'size': 50}), 'current_city': forms.TextInput(attrs={'size': 50}), 'neighbour_hood': forms.TextInput(attrs={'size': 50}), 'current_employment': forms.TextInput(attrs={'size': 50}), 'message': forms.Textarea(attrs={'rows': 15, 'cols': 50}), 'file_upload': ClearableFileInput(attrs={'multiple': True})
        }
        # widgets is important to upload multiple files
