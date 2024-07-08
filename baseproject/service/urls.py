from django.urls import path, re_path
from .views import *

app_name = 'service'

urlpatterns = [
    path('', service, name='service')
]