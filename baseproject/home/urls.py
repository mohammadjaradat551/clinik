from django.urls import path, re_path
from .views import doctors

app_name = 'home'

urlpatterns = [
    path('',doctors, name='doctors'),
]