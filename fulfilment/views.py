from django.shortcuts import render
from django.shortcuts import HttpResponse


def fulfilment_page(request):
    template = 'fulfilment/main.html'
    context = {}





    return render(request, template, context)
