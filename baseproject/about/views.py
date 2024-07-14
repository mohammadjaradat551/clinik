from django.shortcuts import render
from .models import About
# Create your views here.

#about section
def about(request):
    context= {
        'about':About.objects.first(),
    }
    return render(request, 'about.html', context)