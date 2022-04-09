from django.urls import path

from .views import SignUp,DoctorSignUpView,PatientSignUpView,main,doctor,patient
urlpatterns = [
  path('signup/',SignUp,name='signup'),
  path('accounts/signup/doctor/', DoctorSignUpView.as_view(), name='doctor_signup'),
  path('accounts/signup/patient/', PatientSignUpView.as_view(), name='patient_signup'),
  path('main/',main,name='main'),
  path('doctor/',doctor,name='doctor'),
   path('patient/',patient,name='patient'),
]