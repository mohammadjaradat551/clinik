from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Section(models.Model):
    section_name = models.CharField(max_length=50, primary_key= True)
    icon_name = models.CharField(max_length=100, default="")
    description = models.TextField(default="")


    def __str__(self):
        return self.section_name

class Doctors(models.Model):
    doctor_name = models.CharField(max_length=100)
    section=models.ForeignKey(Section, on_delete=models.CASCADE, related_name='doctors_section')
    doctor_image= models.ImageField(default="", upload_to='appointment/')
    
    def __str__(self):
        return self.doctor_name

class TakeAppointment(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointment_owner')
    section= models.ForeignKey(Section, on_delete=models.CASCADE, related_name='appointment_section')
    doctor= models.ForeignKey(Doctors, on_delete=models.CASCADE, related_name='appointment_doctors')
    phone= models.CharField(max_length=15)
    appointment_date= models.DateField(default=timezone.now)
    appointment_time= models.TimeField(default=timezone.now)
    

    def __str__(self):
        return f"{self.doctor} - {self.appointment_date}"



