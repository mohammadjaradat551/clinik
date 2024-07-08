from django.urls import path, re_path
from .views import *

app_name = 'about'

urlpatterns = [
    path('', about, name='about')
]