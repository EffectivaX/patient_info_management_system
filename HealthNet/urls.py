from django.urls import path, include
from django.conf.urls import url
from .forms import PatientModelForm
from . import views

urlpatterns = [
    path('HealthNet/', views.index, name='index'),
    path('HealthNet/patients/view_all/', views.view_all, name='all_patients'),
    path('HealthNet/patients/patient_form/', views.patient_form, name='patients/patient_form'),
    path('HealthNet/patients/patient_info/<int:id>/', views.patient_info, name='patient_info'),
    path('HealthNet/patients/get_reports/', views.get_reports, name="reports"),
    path('HealthNet/patients/new_patient/', views.new_patient, name="New Patient")
    # path('add_patient', views.add_patient, name='new_patient'),
    # path('patient_info/<uuid:pk/$>', views.patient_info, name='patient_info'),
]