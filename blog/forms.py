from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'website', 'body',)
        widgets = {'name': forms.TextInput(attrs={'size': 50}), 'email': forms.TextInput(attrs={'size': 50}), 'website': forms.TextInput(attrs={'size': 50}), 'body': forms.Textarea(attrs={'rows': 20, 'cols': 50})}
