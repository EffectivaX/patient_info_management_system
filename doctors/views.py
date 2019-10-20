
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator

# Create your views here.
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'index.html'


def index(request):
    context = {'title': 'Patient Dashboard'}

    return render(request, 'doctors/index.html', context)


def view_all(request):
    template_name = 'view_doctors.html'
    doctors = doctors.objects.all()
    paginator = Paginator(doctors, 10)

    context = {
        'title': 'All doctors'
    }
    return render(request, 'doctors/view_doctors.html', context)

def patient_info(request):
    template_name = 'detail_patient.html'

    context = {
        'title': 'Detailed Information on patient.name' 
    }
    return render(request, 'doctors/detail_patient.html')    
