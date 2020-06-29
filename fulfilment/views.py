from django.shortcuts import render
from django.shortcuts import HttpResponse
from . import forms
from . import models
import pandas as pd
import csv


def fulfilment_page(request):
    template = 'fulfilment/main.html'
    form_data = forms.UploadFileForm()
    form_letter = forms.DownloadLetterForm()
    model = models.FulfilmentFilesData.objects.all()
    uploaded = False
    records_count = 0


#--------------------IMPORTS--------------------------------------------
    if request.method == 'POST':
        form = forms.UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file_path']
            path = form.cleaned_data['file_path']
            data = file.read().decode('UTF-8').splitlines()
            dic_data = csv.DictReader(data)
            form = form.save(commit=False)
            form.file_name = file
            form.user_id = 'izipizi'


#------FourPaws----

            if request.POST.get('fourpaws_upload'):
                model.delete()
                for row in dic_data:

                    model.create(
                        charity_name            = 'fourpaws',
                        file_name               = form.file_name,
                        title                   = row['title'],
                        firstname               = row['forename'],
                        surname                 = row['surname'],
                        add1                    = row['address1'],
                        add2                    = row['address2'],
                        add3                    = row['address3'],
                        town                    = row['town'],
                        county                  = row['county'],
                        postcode                = row['postcode'],
                        country                 = row['country'],
                        card_holders_name       = row['card_holders_name'],
                        bank_account_number     = row['bank_account_number'],
                        first_collection_date   = row['collection_date'],
                        amount                  = row['amount'],
                        frequency               = row['frequency']
                    )
                    records_count += 1
                models.UploadFile.objects.all().delete()
                form.save()

    context = {
        'form_data': form_data,
        'form_letter': form_letter,
        'uploaded': uploaded,
        'records_count': records_count,
        'model': model,
        'model2': models.UploadFile.objects.all()
    }


    return render(request, template, context)
