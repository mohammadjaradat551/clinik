from django.db import models

# Create your models here.

class Clinic(models.Model):
    site_name= models.CharField(max_length=50)
    phone= models.CharField(max_length=15)
    email= models.EmailField(max_length=255)
    address= models.CharField(max_length=500)
    opening_dateTime= models.DateTimeField()
    facebook= models.URLField(max_length = 200)
    x= models.URLField(max_length = 200)
    linkedIn= models.URLField(max_length = 200)
    Instagram= models.URLField(max_length = 200)

    def __str__(self):
        return self.site_name

    
    
