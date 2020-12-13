from django.urls import path, include
from cars.views import get_cars, car_detail, delete_car

urlpatterns = [
    path('cars/', get_cars, name='cars'),
    path('cars/<int:car_id>/', car_detail, name='car detail'),
    path('cars/delete/<int:car_id>/', delete_car, name='delete car'),
]
