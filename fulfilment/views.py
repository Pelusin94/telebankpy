from django.shortcuts import render
from . import forms
from . import models
import csv
from .mapping import CharityMapping


def fulfilment_page(request):
    template = 'fulfilment/main.html'
    form_data = forms.UploadFileForm()
    form_letter = forms.DownloadLetterForm()
    model = models.FulfilmentFilesData.objects.all()
    records_count = 0
    charity_name = request.session.get('charity_name')


    if request.method == 'POST':
        form = forms.UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file_path']
            data = file.read().decode('UTF-8').splitlines()
            dic_data = csv.DictReader(data)
            # FILLING REMAING MODEL'S FIELDS
            form = form.save(commit=False)
            form.file_name = file
            form.user_id = request.user.username
            form.charity_name = charity_name
            # MAPPING AND IMPORTING DATA ACCORDING TO THE CHARITY SPECS AND RETREAVE NUMBER OF RECORDS IMPORTED
            data_import = CharityMapping(charity_name, model, file, dic_data)
            records_count = data_import.mapper()
            # SAVINTG PHYSICAL COPY
            form.save()


    if request.method == 'GET':
        form = forms.DownloadLetterForm(request.GET)
        if form.is_valid():
            date_from = form.cleaned_data['date_from']
            date_to = form.cleaned_data['date_to']


    context = {
        'form_data': form_data,
        'form_letter': form_letter,
        'records_count': records_count,
        'charity': charity_name,
        'model': model,
        'model2': models.UploadFile.objects.all(),
    }


    return render(request, template, context)
