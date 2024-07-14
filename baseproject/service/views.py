from django.shortcuts import render
from appointment.models import Section
from home.models import Clinic
# Create your views here.

#service name and description and icon
#email and phone
#appointment section
def service(request):
    
    context = {
        'services':Section.objects.all(),
        'clinic':Clinic.objects.first(),
    }
    return render(request, 'service.html', context)