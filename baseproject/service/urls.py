from django.urls import path, re_path
from .views import *

app_name = 'service'

urlpatterns = [
    path('', ServiceView.as_view(), name='service')
]