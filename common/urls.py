from django.urls import path

from common.views import index_page

urlpatterns = [
    path('', index_page, name='index')
]