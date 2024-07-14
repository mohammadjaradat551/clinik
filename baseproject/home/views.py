from django.shortcuts import render
from appointment.models import Doctors, TakeAppointment
from .models import Clinic

# Create your views here.

#total doctors
#total patients(count who makes appointmnet )
#all doctors
#phone and email of clinic
#the appointment operation
def home(request):
    total_doctors= Doctors.objects.count()
    total_patients= TakeAppointment.objects.count()
    doctors= Doctors.objects.all()
    clinic= Clinic.objects.first()
    
    context= {
        'total_doctors':total_doctors,
        'total_patients':total_patients,
        'doctors':doctors,
        'clinic':clinic,
    }
    return render(request, 'home.html', context)
