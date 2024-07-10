from django.contrib import admin
from .models import Clinic

# Register your models here.




admin.site.register(Clinic)

# class ClinicAdmin(admin.ModelAdmin):
#     list_display = ('name', 'opening_datetime')
#     search_fields = ('name',)
