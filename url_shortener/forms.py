from django import forms
from .models import Link


class LinkShortenerForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['long_url']
        labels = {
            'long_url': 'Your URL:',
        }