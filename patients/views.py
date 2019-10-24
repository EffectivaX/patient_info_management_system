from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect

# Create your views here.
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from .models import Patient
from .forms import PatientRegistrationForm


class PatientView(FormView):
    form_class = PatientRegistrationForm
    template_name = 'add_patient.html'
    success_url = reverse_lazy('success')

def index(request):
    context = {'title': 'Patient Dashboard'}

    return render(request, 'patients/index.html', context)


def add_patient(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST or None)
        if form.is_valid():
            form_user_data = PatientRegistrationForm(request.POST)
            #Process the data i form.cleaned_data as required
            #...
            # redirect to a new URL:
            return HttpResponseRedirect('/patients/view_all')
    else:
        form = PatientRegistrationForm

    
    context = {
        'form': form
    }   

    return render(request, 'patients/add_patient.html', context)


def view_all(request):
    template_name = 'view_patients.html'
    patients = Patient.objects.all()
    paginator = Paginator(patients, 10)

    context = {'title': 'All Patients'}
    return render(request, 'patients/view_patients.html', context)


def patient_info(request):
    template_name = 'detail_patient.html'

    context = {'title': 'Detailed Information on patient.name'}
    return render(request, 'patients/detail_patient.html')