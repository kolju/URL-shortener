from django import forms


class LinkShortenerForm(forms.Form):
    url = forms.URLField(label='Your URL:')
