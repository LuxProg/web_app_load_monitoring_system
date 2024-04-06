from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('whoweare/', whoweare),
    path('feedback/', feedback),
    path('dip_work_page/<int:dip_id>', dip_work_page, name='dwp'),
]