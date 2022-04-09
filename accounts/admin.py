from django.contrib import admin
from accounts.models import User,Doctor,Patient

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_dispay=['is_doctor','is_patient']
admin.site.register(User,UserAdmin)

class DoctorAdmin(admin.ModelAdmin):
    list_dispay=['user','firstname','lastname','email','password','confirmpassword','Address']
admin.site.register(Doctor,DoctorAdmin)

class PatientrAdmin(admin.ModelAdmin):
    list_dispay=['user','firstname','lastname','email','password','confirmpassword','Address']
admin.site.register(Patient,PatientrAdmin)
