from django import forms
from .models import TakeAppointment

class TakeAppointmentForm(forms.ModelForm):
    
    class Meta:
        model = TakeAppointment
        fields = ['section','doctor','phone','appointment_date','appointment_time']

        widgets = {
            'section':forms.Select(attrs={'class':'form-control'}),
            'doctor':forms.Select(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            

        }

    def save(self, commit= True):
        # Call the parent class's save method to get the unsaved instance(not yet saved to the database.)
        appointment = super().save(commit= False)
        # Set the user attribute to the current user
        appointment.user= self.user
        if commit:
            appointment.save()
        return appointment
