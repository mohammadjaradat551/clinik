from django.shortcuts import redirect, render
from .forms import TakeAppointmentForm
# Create your views here.

#appointment section
#mail and phone
def make_appointment(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form= TakeAppointmentForm(request.POST)
        if form.is_valid():
            form.user= request.user
            form.save()
            return redirect("home")
    else :
        form= TakeAppointmentForm()

    return render(request, 'appointment/appointment.html', {'form':form})