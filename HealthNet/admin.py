from django.contrib import admin

# Register your models here.
from .models import Patient, Doctor, Staff, HospitalsAndClinics, Contact, MedicalAidScheme

class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth',
                    'purpose_of_visit', 'date_of_visit', 'national_id', 'phone_number', 'email_address')
    prepopulated_fields = {'first_name': ('last_name','purpose_of_visit', )}

class DoctorAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'last_name', 'qualification', 'specialty', 'phone_number','Email']

class StaffAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'position', 'phone_number','Email']

class HospitalsAndClinicsAdmin(admin.ModelAdmin):
    list_display = ['name']

class MedicalRecordsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth',
                    'blood_type', 'created_at')
    prepopulated_fields = {'first_name' : ('last_name', 'physical_address')}

class MedicalAidSchemeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    prepopulated_fields = {'name' : ('email', 'message')}


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)
# admin.site.register(MedicalRecords, MedicalRecordsAdmin)
admin.site.register(HospitalsAndClinics, HospitalsAndClinicsAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(MedicalAidScheme, MedicalAidSchemeAdmin)
