from django import forms
from . import models
from django.utils.translation import gettext_lazy as lazy


class UploadFileForm(forms.ModelForm):
    class Meta:
        model   = models.UploadFile
        exclude = ['upload_date']
        widgets = {
            'file_name': forms.HiddenInput(),
            'user_id': forms.HiddenInput(),
        }
        labels = {
            'file_path': lazy('File')
        }


class DownloadLetterForm(forms.Form):
    date_from = forms.CharField(widget=forms.DateInput(attrs={'type': 'date'}))
    date_to = forms.CharField(widget=forms.DateInput(attrs={'type': 'date'}))


