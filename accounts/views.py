from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from accounts.forms import UserRegisterForm, UserLoginForm


def user_profile(request):
    return render(request, 'accounts/profile.html')


def get_redirect_url(params):
    redirect_url = params.get('return_url')
    return redirect_url if redirect_url else 'index'


def signin_user(request):
    if request.method == 'GET':
        context = {
            'login_form': UserLoginForm(),
        }

        return render(request, 'accounts/signin.html', context)
    else:
        login_form = UserLoginForm(request.POST)

        return_url = get_redirect_url(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect(return_url)

        context = {
            'login_form': login_form,
        }

        return render(request, 'accounts/signin.html', context)


def signup_user(request):
    if request.method == 'GET':
        context = {
            'form': UserRegisterForm(),
        }

        return render(request, 'accounts/signup.html', context)
    else:
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect('user profile')

        context = {
            'form': form,
        }

        return render(request, 'accounts/signup.html', context)


def logout_user(request):
    logout(request)
    return redirect('index')
