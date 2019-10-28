from django.urls import path, include
from .forms import PatientForm
from . import views

urlpatterns = [
    path('patients/', views.index, name='index'),
    path('view_all', views.view_all, name='all_patients'),
    path('add_patient', views.add_patient, name='new_patient'),
    path('patient_info', views.patient_info, name='patient_info'),
    path('patient_form', views.patient_form, name='form')
    # path('', include('patients.urls')),
    # path('', HomePageView.as_view(), name='home'),
]