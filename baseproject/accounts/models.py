from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, related_name='user_profile', on_delete=models.CASCADE)
    tc= models.CharField(max_length=15)
    image = models.ImageField(upload_to='profile/'  , blank=True, null=True)
    phone_number = models.CharField(max_length=16 , blank=True, null=True)
    email = models.CharField(max_length=50 , blank=True, null=True)

    def __str__(self):
        return str(self.user)