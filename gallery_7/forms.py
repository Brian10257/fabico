from django import forms
from django.forms import ClearableFileInput
from .models import Gallery7


class Gallery7ModelForm(forms.ModelForm):
    class Meta:
        model = Gallery7
        fields = ['file_upload']
        widgets = {
            'file_upload': ClearableFileInput(attrs={'multiple': True}),
        }
        # widgets is important to upload multiple files
 