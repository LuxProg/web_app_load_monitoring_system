from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('whoweare/', whoweare),
    path('feedback/', feedback),
    path('diplom/<int:dip_id>/', dip_work),
]