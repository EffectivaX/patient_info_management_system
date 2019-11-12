from django.contrib import admin

# Register your models here.
from .models import Patient, Doctor, HospitalStaff, MedicalRecords, Contact

class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth',
                    'purpose_of_visit', 'medical_aid_group', 'date_of_visit')
    prepopulated_fields = {'first_name': ('last_name','purpose_of_visit', )}

class DoctorAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'last_name', 'qualification', 'specialty', 'phone_number','Email']

class HospitalStaffAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    prepopulated_fields = {'first_name' : ('last_name', 'identification_id',)}

class MedicalRecordsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth',
                    'blood_type', 'medical_aid_group', 'created_at')
    prepopulated_fields = {'first_name' : ('last_name', 'physical_address')}

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'category', 'message')
    prepopulated_fields = {'name' : ('email', 'category')}


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(HospitalStaff, HospitalStaffAdmin)
admin.site.register(MedicalRecords, MedicalRecordsAdmin)
admin.site.register(Contact, ContactAdmin)
