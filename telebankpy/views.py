from django.shortcuts import render
from django.http import HttpResponse

def main_page(request):
    template = 'telebankpy/main.html'
    context = {}
    return render(request, template, context)