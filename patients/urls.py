from django.urls import path, include
from django.conf.urls import url
from .forms import PatientModelForm
from . import views

urlpatterns = [
    path('patients/', views.index, name='index'),
    path('patients/view_all/', views.view_all, name='all_patients'),
    path('patients/patient_form/', views.patient_form, name='patients/patient_form'),
    path('patients/patient_info/<int:id>/', views.patient_info, name='patient_info'),
    path('patients/get_reports/', views.get_reports, name="reports"),
    path('patients/new_patient/', views.new_patient, name="New Patient")
    # path('add_patient', views.add_patient, name='new_patient'),
    # path('patient_info/<uuid:pk/$>', views.patient_info, name='patient_info'),
]