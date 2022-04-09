from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.views.generic import CreateView
from .forms import PatientSignUpForm,DoctorSignUpForm
from.models import User,Doctor

# Create your views here.
def SignUp(request):
    return render(request,'register.html')

def main(request):
    return render(request,'main.html')

def doctor(request):
    return render(request,'doctor.html')

def patient(request):
    return render(request,'patient.html')


class DoctorSignUpView(CreateView):
    model=User
    form_class=DoctorSignUpForm
    template_name='signup.html'

    def get_context_data(self,**kwargs):
        kwargs['user_type']='doctor'
        return super().get_context_data(**kwargs)

    def form_valid(self,form):
        user=form.save()
        login(self.request,user)
        return redirect('doctor')
        
        
        
        

class PatientSignUpView(CreateView):
    model=User
    form_class=PatientSignUpForm
    template_name='signup.html'

    def get_context_data(self,**kwargs):
        kwargs['user_type']='patient'
        return super().get_context_data(**kwargs)

    def form_valid(self,form):
        user=form.save()
        #login(self.request, user)
        return redirect('patient')





