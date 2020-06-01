from django.shortcuts import render
from django.contrib.auth import login, get_user_model, logout

# PasswordResetView,PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

from django.http import HttpResponseRedirect

from .forms import UserCreationForm, UserLoginForm

def register(request, *args, **kwargs):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/login')
    context = {
        'form': form,
        'title' : 'ProHealthnet Register',
        'button' : 'Register',
        'alt_page' : '/login/',
        'page_text' : 'Already Registered?',
        'button_option' : 'Login'
    }

    return render(request, 'accounts/register.html', context)

def login_view(request, *args, **kwargs):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        user_obj = form.cleaned_data.get('user_obj')
        login(request, user_obj)
        return HttpResponseRedirect('/HealthNet/')
    context = {
        'form': form,
        'title' : 'ProHealthnet Login',
        'button' : 'Login',
        'alt_page' : '/register/',
        'page_text' : 'Not Registered Yet?',
        'button_option' : 'Register'
    }

    return render(request, 'accounts/login.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')
