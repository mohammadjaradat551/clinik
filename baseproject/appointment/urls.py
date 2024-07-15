from django.urls import path, re_path
from .views import *

app_name = 'appointment'

urlpatterns = [
    path('', MakeAppointmentView.as_view(), name='appointment'),
    #path('my_appointment/', my_appointment, name='my_appointment'),

]