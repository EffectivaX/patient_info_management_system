from django.urls import path, include
# from . import views
from . import views

urlpatterns = [
    path('doctors/', views.index, name='index'),
    path('view_all', views.view_all, name='all_doctors'),
    path('doctor_info', views.patient_info, name='doctor_info')
]