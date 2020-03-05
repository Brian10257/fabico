from django import forms
from django.forms import ClearableFileInput
from .models import Gallery1


class Gallery1ModelForm(forms.ModelForm):
    class Meta:
        model = Gallery1
        fields = ['file_upload']
        widgets = {
            'file_upload': ClearableFileInput(attrs={'multiple': True}),
        }
        # widgets is important to upload multiple files
