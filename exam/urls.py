from django.urls import path, include
from exam.views import start_exam

urlpatterns = [
    path('start/', start_exam, name='start exam'),
]