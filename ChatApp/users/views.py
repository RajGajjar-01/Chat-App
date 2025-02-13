from . import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

def register_view(request):
    if request.method == 'POST':
        register_form = forms.UserRegistrationForm(request.POST, auto_id=True)
        if register_form.is_valid():
            print(register_form.cleaned_data)
            register_form.save()
            return redirect('login')
    else :
        register_form = forms.UserRegistrationForm(auto_id=True)
    
    context = {
        'form' : register_form,
        'title': 'sign up'
    }
    return render(request, 'users/Register.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')
