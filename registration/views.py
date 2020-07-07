from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def main_page(request):
    template = 'registration/main.html'
    context = {}
    return render(request, template, context)


def login_page(request):
    template = 'registration/login.html'
    form = forms.UploadFileForm()

    if request.method == 'POST':
        form = forms.UploadFileForm(request.POST)

        if form.is_valid():
            charity_name = form.cleaned_data['charity_name']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            login(request,user)
            return HttpResponse('izi pizi')

    context = {
        'form':form
    }
    return render(request, template, context)