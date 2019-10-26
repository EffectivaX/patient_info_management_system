from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect

# Create your views here.
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from .models import Patient
from .forms import PatientForm #, PatientSnippetForm

# class PatientView(FormView):
#     form_class = PatientForm
#     template_name = 'add_patient.html'
#     success_url = reverse_lazy('success')


def index(request):
    context = {'title': 'Patient Dashboard'}

    return render(request, 'patients/index.html', context)


# def add_patient(request):
#     if request.method == 'POST':
#         form = PatientForm(request.POST)
#         if form.is_valid():
#             prefix = form.cleaned_data['prefix']
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             date_of_birth = form.cleaned_data['date_of_birth']
#             gender = form.cleaned_data['gender']
#             home_address = form.cleaned_data['home_address']
#             national_id = form.cleaned_data['national_id']
#             phone_number_ = form.cleaned_data['phone_number']
#             email_address = form.cleaned_data['email_address']
#             purpose_of_visit = form.cleaned_data['purpose_of_visit']
#             description_of_the_condition = form.cleaned_data[
#                 'description_of_the_condition']
#             blood_type = form.cleaned_data['blood_type']
#             current_medication = form.cleaned_data['current_medication']
#             body_mass = form.cleaned_data['body_mass']
#             allergies = form.cleaned_data['allergies']
#             employment_status = form.cleaned_data['employment_status']
#             consulted_doctor = form.cleaned_data['consulted_doctor']
#             marital_status = form.cleaned_data['marital_status']
#             medical_aid_group = form.cleaned_data['medical_aid_group']
#             date_of_visit = form.cleaned_data['date_of_visit']
#             #Process the data i form.cleaned_data as required
#             #...
#             # redirect to a new URL:
#             # form.save()
#             return HttpResponseRedirect('/patients/view_all')
#     else:
#         form = PatientForm

#     context = {'form': form}

#     return render(request, 'patients/form.html', context)

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient_info = form.save(commit=False)
            patient_info.save()
    else:
        form = PatientForm()

    context = {'form': form}

    return render(request, 'patients/form.html', context)



def snippet_detail(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient_info = form.save(commit=False)
            patient_info.save()
    else:
        form = PatientForm()

    context = {'form': form}

    return render(request, 'patients/form.html', context)


def view_all(request):
    template_name = 'view_patients.html'
    # patients = Patient.objects.all()
    # paginator = Paginator(patients, 10)

    context = {'title': 'All Patients'}
    return render(request, 'patients/view_patients.html', context)


def patient_info(request):
    template_name = 'detail_patient.html'

    context = {'title': 'Detailed Information on patient.name'}
    return render(request, 'patients/detail_patient.html')