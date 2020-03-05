from django import forms
from django.forms import ClearableFileInput
from .models import Gallery3


class Gallery3ModelForm(forms.ModelForm):
    class Meta:
        model = Gallery3
        fields = ['file_upload']
        widgets = {
            'file_upload': ClearableFileInput(attrs={'multiple': True}),
        }
        # widgets is important to upload multiple files
