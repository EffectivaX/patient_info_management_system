from django.urls import path, include
from django.conf.urls import url
from .forms import PatientForm, ContactForm, DoctorForm
from . import views

urlpatterns = [
    # Patient urls
    path('HealthNet/', views.index, name='index'),
    path('HealthNet/patients/view_all/', views.view_all, name='All Patients'),
    path('HealthNet/patients/patient_form/', views.patient_form, name='Patient Form'),
    path('HealthNet/patients/patient_info/<int:id>/', views.patient_info, name='patient_info'),
    path('HealthNet/patients/edit_patient/<int:pk>/', views.edit_patient, name='edit_info'),
    path('HealthNet/patients/delete_patient/<int:id>/', views.delete_patient, name='Delete'),
    # path('HealthNet/patients/DeletePatient/<int:id>/', views.PatientDelete.as_view(), name='Delete Patient'),
    path('HealthNet/patients/reports/', views.reports, name="reports"),
    # path('HealthNet/patients/edit_patient/<int:id>/', views.PatientFormUpdate.as_view(), name='Update Patient'),

    # Contact Page url
    path('HealthNet/GetInTouch/', views.contact_form, name='Contact'),
    path('HealthNet/messages/', views.read_messages, name="Read Messages"),

    # Staff Members urls
    path('HealthNet/staff/doctors/', views.all_doctors, name='Medical Staff'),
    path('HealthNet/staff/add_doctor/', views.add_doctor, name='Add Doctor'),
    path('HealthNet/staff/new_member/', views.add_staff_member, name="Add Staff Member"),
    path('HealthNet/staff/all_members/', views.all_members, name='All Members'),
    path('HealthNet/staff/update_doctor/<int:id>/', views.update_doctor, name='Edit Staff Member'),
    path('HealthNet/staff/edit_member/<int:id>/', views.update_member, name='Edit Staff Member'),
    path('HealthNet/staff/delete_member/<int:id>/', views.delete_staff_member, name='Delete Member'),
    path('HealthNet/staff/delete_doctor/<int:id>/', views.delete_doctor, name='Delete Doctor')
]

# urlpatterns += staticfiles_urlpatterns()
