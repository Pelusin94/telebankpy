from django.shortcuts import render
from django.shortcuts import HttpResponse
from . import forms
from . import models
import pandas as pd


def fulfilment_page(request):
    template = 'fulfilment/main.html'
    form_data = forms.UploadFileForm()
    form_letter = forms.DownloadLetterForm()
    model = models.FulfilmentFilesData.objects.all()
    uploaded = False
    row_count = 0

    context = {
        'form_data': form_data,
        'form_letter': form_letter,
        'uploaded': uploaded,
    }

    if request.method == 'POST':
        form = forms.UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file_path']
            name = form.cleaned_data['file_name']
            data = pd.read_csv(file)

#-------------------------FourPaws---------------------------
            if request.POST.get('fourpaws_upload'):
                for row in data.iterrows():
                    print(row[1])




    return render(request, template, context)
