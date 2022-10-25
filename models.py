from email import message
from email.headerregistry import Address
from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=50)
    email  = models.EmailField(max_length=50)
    bio = models.CharField(max_length=70)
    def __str__(self):
        return self.name

