from django.shortcuts import render, redirect
from appointment.models import Doctors, TakeAppointment
from .models import Clinic
from appointment.views import MakeAppointmentView
from appointment.forms import TakeAppointmentForm

# Create your views here.

class HomeView(MakeAppointmentView):
    template_name = 'home.html'  
    def get(self, request):
        total_doctors = Doctors.objects.count()
        total_patients = TakeAppointment.objects.count()
        doctors = Doctors.objects.all()
        clinic = Clinic.objects.first()
        
        # Add the appointment form to the context
        section_name = request.GET.get('section')
        form = TakeAppointmentForm(section_name=section_name)
        
        context = {
            'total_doctors': total_doctors,
            'total_patients': total_patients,
            'doctors': doctors,
            'clinic': clinic,
            'form': form,
        }
        return render(request, self.template_name, context)
    

    def post(self, request):
        section_name = request.POST.get('section')
        form = TakeAppointmentForm(request.POST, section_name=section_name)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect("/")
        # Get the context data again for the post request
        total_doctors = Doctors.objects.count()
        total_patients = TakeAppointment.objects.count()
        doctors = Doctors.objects.all()
        clinic = Clinic.objects.first()
        
        context = {
            'total_doctors': total_doctors,
            'total_patients': total_patients,
            'doctors': doctors,
            'clinic': clinic,
            'form': form,
        }
        return render(request, self.template_name, context)
    
    