from django import forms

from .models import FileRequest

class RequestForm(forms.ModelForm):
    class Meta:
        model = FileRequest
        fields = {
            'title',
            'fileName'
        }