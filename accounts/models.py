from email.headerregistry import Address
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_doctor=models.BooleanField(default=False)
    is_patient=models.BooleanField(default=False)

class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    email=models.CharField(max_length=100)
    #password=models.CharField(max_length=200)
    #confirmpassword=models.CharField(max_length=200)
    Address=models.CharField(max_length=200)
    
    def __str__(self):
        return self.user.username

class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    email=models.CharField(max_length=100)
    #password=models.CharField(max_length=200)
    #confirmpassword=models.CharField(max_length=200)
    Address=models.CharField(max_length=200)
    
    def __str__(self):
        return self.user.username


