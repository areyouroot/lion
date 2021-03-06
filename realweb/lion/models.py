from distutils.command.upload import upload
from email.mime import image
from email.policy import default
import imp
from django.db import models
from django.contrib.auth.models import User

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default = 'default.jpg',upload_to = 'profile_pics')
    password = models.CharField(max_length=60)

    def __str__(self):

        return f'{self.user.username} profile'
        

# Create your models here.
