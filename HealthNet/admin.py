from django.contrib import admin

# Register your models here.
from .models import Patient
from .models import Doctor

class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth',
                    'purpose_of_visit', 'medical_aid_group', 'date_of_visit')
    prepopulated_fields = {'first_name': ('last_name','purpose_of_visit', )}

class DoctorAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'last_name', 'qualification', 'specialty']
    
    
admin.site.register(Doctor, DoctorAdmin)    
admin.site.register(Patient, PatientAdmin)
