from django.shortcuts import render

# Create your views here.

#service name and description and icon
#email and phone
#appointment section
def service(request):
    return render(request, 'service.html')