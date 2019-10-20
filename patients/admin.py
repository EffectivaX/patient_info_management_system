from django.contrib import admin
from .models import Patient
# from .forms import PatientRegistrationForm

# Register your models here.


class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'purpose_of_visit', 'slug')
    prepopulated_fields = {'slug': ('slug', )}


admin.site.register(Patient, PatientAdmin)
# admin.site.register(PatientRegistrationForm)
