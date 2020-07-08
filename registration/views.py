from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import reverse, redirect
from . import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def main_page(request):
    template = 'registration/main.html'
    context = {}
    return render(request, template, context)


def logout_page(request):
    logout(request)
    return redirect(main_page)


def login_page(request):
    template = 'registration/login.html'
    form = forms.UploadFileForm()

    if request.method == 'POST':
        form = forms.UploadFileForm(request.POST)

        if form.is_valid():
            charity_name = form.cleaned_data['charity_name']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    request.session['charity_name'] = charity_name
                    return redirect(main_page)

    context = {
        'form': form
    }
    return render(request, template, context)