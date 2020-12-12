from django.urls import path, include
from exam.views import start_exam, exam_result

urlpatterns = [
    path('start/', start_exam, name='start exam'),
    path('result/', exam_result, name='exam result')
]