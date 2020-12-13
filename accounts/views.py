from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from accounts.forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.models import User
import os
from cars.forms import CarCreateForm
from cars.models import Car
from exam.models import Result


@login_required
def user_profile(request):
    user = request.user
    if request.method == 'GET':

        if Car.objects.get(fk_user_id=user.id):
            get_car = Car.objects.get(fk_user_id=user.id)

        context = {
            'user': user,
            'results': Result.objects.filter(fk_user_id=user.id),
            'form': CarCreateForm(),
            'car': get_car,
        }

        return render(request, 'accounts/profile.html', context)
    if request.method == 'POST':
        car = Car.objects.get(fk_user_id=user.id)
        old_image = car.car
        form = CarCreateForm(
            request.POST,
            request.FILES,
            instance=car
        )

        if form.is_valid():
            if old_image:
                delete_old_image(old_image.path)
            form.save()

            return redirect('user profile')

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
        has_next = request.GET.get('next')

        if has_next:
            return_url = has_next
        else:
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
            car = Car()
            user = form.save()
            user_model = User.objects.get(id=user.id)
            car.fk_user_id = user_model
            car.car = ''
            car.save()
            login(request, user)
            return redirect('user profile')

        context = {
            'form': form,
        } 

        return render(request, 'accounts/signup.html', context)


def logout_user(request):
    logout(request)
    return redirect('index')


def delete_old_image(path):
    os.remove(path)
