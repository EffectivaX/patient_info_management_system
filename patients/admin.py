from django.contrib import admin

# Register your models here.
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth',
                    'purpose_of_visit', 'date_of_visit')
    prepopulated_fields = {'slug': ('slug', )}


admin.site.register(Patient, PatientAdmin)
