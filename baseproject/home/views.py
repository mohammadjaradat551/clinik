from django.shortcuts import render

# Create your views here.

#total doctors
#total patients(count who makes appointmnet )
#all doctors
#phone and email of clinic
#the appointment operation
def home(request):
    return render(request, 'home.html')
