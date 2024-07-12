from django.shortcuts import redirect, render
from .forms import TakeAppointmentForm

# Create your views here.

#appointment section
#mail and phone


def make_appointment(request):
    section_name = request.POST.get('section')
    print(f" section name: {section_name}")
    if request.method == 'POST':
        form = TakeAppointmentForm(request.POST, section_name=section_name)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect("/")
    else:
        form = TakeAppointmentForm(section_name=section_name)

    return render(request, 'appointment/appointment.html', {'form': form})
