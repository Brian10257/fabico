from django import forms
from django.forms import ClearableFileInput
from .models import Gallery6


class Gallery6ModelForm(forms.ModelForm):
    class Meta:
        model = Gallery6
        fields = ['file_upload']
        widgets = {
            'file_upload': ClearableFileInput(attrs={'multiple': True}),
        }
        # widgets is important to upload multiple files
 