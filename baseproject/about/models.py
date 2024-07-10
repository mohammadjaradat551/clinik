from django.db import models

# Create your models here.
class About(models.Model):
    about_us = models.CharField(max_length=1000)
    
    
    def __str__(self):
        return self.about_us