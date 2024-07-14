from django.db import models

# Create your models here.

#i didn't work on this
class Service(models.Model):
    service_name = models.CharField(max_length=100)
    description = models.TextField()
    icon_name = models.CharField(max_length=100, default="")

    
    def __str__(self):
        return self.service_name
