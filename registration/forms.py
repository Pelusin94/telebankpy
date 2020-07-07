from django import forms
from . import models


class UploadFileForm(forms.Form):

    charity_choices = [
        (charity.system_name, charity.display_name) for charity in models.CharityNames.objects.all()
    ]

    charity_name = forms.CharField(max_length=100, widget=forms.Select(choices=charity_choices))
    username = forms.CharField(max_length=100, required=True, label='User')
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

