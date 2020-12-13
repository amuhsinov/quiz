from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from cars.models import Car


def car_detail(request, car_id):
    if request.method == 'GET':

        context = {
            'car': Car.objects.get(id=car_id),
        }

        return render(request, 'cars/car_detail.html', context)


def get_cars(request):
    if request.method == 'GET':

        context = {
            'cars': Car.objects.select_related(),
        }

        return render(request, 'cars/cars.html', context)


@login_required
def delete_car(request, car_id):
    if request.method == 'POST':
        Car.objects.filter(id=car_id).update(car='', name='')
        return redirect('user profile')

