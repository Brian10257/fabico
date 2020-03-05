from django import forms
from django.forms import ClearableFileInput
from .models import Gallery5


class Gallery5ModelForm(forms.ModelForm):
    class Meta:
        model = Gallery5
        fields = ['file_upload']
        widgets = {
            'file_upload': ClearableFileInput(attrs={'multiple': True}),
        }
        # widgets is important to upload multiple files
