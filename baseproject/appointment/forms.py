from django import forms
from .models import TakeAppointment, Doctors

class TakeAppointmentForm(forms.ModelForm):
    class Meta:
        model = TakeAppointment
        fields = ['section', 'doctor', 'phone', 'appointment_date', 'appointment_time']
        widgets = {
            'section': forms.Select(attrs={'class': 'form-control'}),
            'doctor': forms.Select(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        section_name = kwargs.pop('section_name', None)
        super().__init__(*args, **kwargs)
        if section_name:
            self.fields['doctor'].queryset = Doctors.objects.filter(section__section_name=section_name)
        else:
            self.fields['doctor'].queryset = Doctors.objects.all()
            print("noneeeee")

    def save(self, commit=True):
        appointment = super().save(commit=False)
        if commit:
            appointment.save()
        return appointment
