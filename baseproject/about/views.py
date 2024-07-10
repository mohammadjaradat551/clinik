from django.shortcuts import render

# Create your views here.

#about section
def about(request):
    return render(request, 'about.html')