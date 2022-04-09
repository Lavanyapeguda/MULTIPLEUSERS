from email.headerregistry import Address
from re import T
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User,Doctor,Patient

class DoctorSignUpForm(UserCreationForm):
    firstname=forms.CharField(required=True)
    lastname=forms.CharField(required=True)
    email=forms.CharField(required=True)
    #password=forms.CharField(required=True)
    #confirmpassword=forms.CharField(required=True)
    Address=forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model=User

    @transaction.atomic
    def save(self):
        user=super().save(commit=False)
        user.firstname=self.cleaned_data.get('firstname')
        user.lastname=self.cleaned_data.get('lastname')
        user.email=self.cleaned_data.get('email')
        #user.password=self.cleaned_data.get('password')
        #user.confirmpasword=self.cleaned_data.get('confirmpassword')
        user.Address=self.cleaned_data.get('Address')
        user.is_doctor=True
        user.save()
        doctor=Doctor.objects.create(user=user)
        return user


class PatientSignUpForm(UserCreationForm):
    firstname=forms.CharField(required=True)
    lastname=forms.CharField(required=True)
    email=forms.CharField(required=True)
    #password=forms.CharField(required=True)
    #confirmpassword=forms.CharField(required=True)
    Address=forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model=User

    @transaction.atomic
    def save(self):
        user=super().save(commit=False)
        user.firstname=self.cleaned_data.get('firstname')
        user.lastname=self.cleaned_data.get('lastname')
        user.email=self.cleaned_data.get('email')
        #user.password=self.cleaned_data.get('password')
        #user.confirmpasword=self.cleaned_data.get('confirmpassword')
        user.Address=self.cleaned_data.get('Address')
        user.is_patient=True
        user.save()
        patient=Patient.objects.create(user=user)
        patient.firstname=self.cleaned_data.get('firstname')
        patient.lastname=self.cleaned_data.get('lastname')
        #patient.password=self.cleaned_data.get('password')
        #patient.confirmpassword=self.cleaned_data.get('confirmpassword')
        patient.Address=self.cleaned_data.get('Address')
        patient.save()

        return patient
        






