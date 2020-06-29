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
    row_count = 0

    context = {
        'form_data': form_data,
        'form_letter': form_letter,
        'uploaded': uploaded,
    }
#--------------------IMPORTS--------------------------------------------
    if request.method == 'POST':
        form = forms.UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file_path']
            file_name = form.cleaned_data['file_name'] = file.name
            user = form.cleaned_data['user_id'] = request.user.username
            path = form.cleaned_data['file_path']
            data = file.read().decode('UTF-8').splitlines()
            dic_data = csv.DictReader(data)
            records_count = 0


#------FourPaws----

            if request.POST.get('fourpaws_upload'):
                for row in dic_data:
                    model.create(
                        charity_name            = 'fourpaws',
                        file_name               = file_name,
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
                form.save()



    return render(request, template, context)
