from .models import Clinic
from appointment.models import Section
def myfooter(request):
    myfooter=Clinic.objects.last()
    sections= Section.objects.all()
    return {'myfooter':myfooter, 'sections':sections}
