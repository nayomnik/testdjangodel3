

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_queue_number', views.get_queue_number, name='get_queue_number'),
]

