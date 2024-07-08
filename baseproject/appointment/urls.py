from django.urls import path, re_path
from .views import *

app_name = 'appointment'

urlpatterns = [
    path('', make_appointment, name='appointment'),
]