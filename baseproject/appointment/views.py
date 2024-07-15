from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import TakeAppointmentForm

class MakeAppointmentView(LoginRequiredMixin, View):
    template_name = 'appointment/appointment.html'
    
    def get(self, request):
        
        section_name = request.GET.get('section')
        form = TakeAppointmentForm(section_name=section_name)
        return render(request, self.template_name, {'form': form, 'section_name': section_name})

    def post(self, request):
        section_name = request.POST.get('section')
        form = TakeAppointmentForm(request.POST, section_name=section_name)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect("/")
        
        return render(request, self.template_name, {'form': form, 'section_name': section_name})