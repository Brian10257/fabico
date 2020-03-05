from django import forms
from django.forms import ClearableFileInput
from .models import Gallery4


class Gallery4ModelForm(forms.ModelForm):
    class Meta:
        model = Gallery4
        fields = ['file_upload']
        widgets = {
            'file_upload': ClearableFileInput(attrs={'multiple': True}),
        }
        # widgets is important to upload multiple files
