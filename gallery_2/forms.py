from django import forms
from django.forms import ClearableFileInput
from .models import Gallery2


class Gallery2ModelForm(forms.ModelForm):
    class Meta:
        model = Gallery2
        fields = ['file_upload']
        widgets = {
            'file_upload': ClearableFileInput(attrs={'multiple': True}),
        }
        # widgets is important to upload multiple files
