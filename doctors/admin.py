from django.contrib import admin
from .models import Doctor

# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'qualification', 'specialty']
    
admin.site.register(Doctor, DoctorAdmin)
