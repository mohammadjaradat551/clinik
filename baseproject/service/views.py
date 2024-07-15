from django.shortcuts import render, redirect
from appointment.models import Section
from home.models import Clinic
from appointment.views import MakeAppointmentView
from appointment.forms import TakeAppointmentForm
# Create your views here.



class ServiceView(MakeAppointmentView):
    template_name= 'service.html'

    def get(self, request):
        section_name=request.GET.get('section')
        form= TakeAppointmentForm(section_name= section_name)

        context = {
        'services':Section.objects.all(),
        'clinic':Clinic.objects.first(),
        'form':form,
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        section_name=request.POST.get('section')
        form= TakeAppointmentForm(request.POST, section_name= section_name)
        if form.is_valid():
            form.instance.user= request.user 
            form.save()
            return redirect('/')
        
        context = {
        'services':Section.objects.all(),
        'clinic':Clinic.objects.first(),
        'form':form,
        }
        return render(request, self.template_name, context)
        