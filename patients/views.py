from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST, require_GET

# Create your views here.
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .models import Patient
from .forms import PatientModelForm #PatientForm  #, PatientSnippetForm


def index(request):
    context = {
        'title': 'Patient Dashboard',
    }

    return render(request, 'patients/index.html', context)

# A function to add new patient to the database
def patient_form(request):
    if request.method == 'POST':
        form = PatientModelForm(request.POST)
        if form.is_valid():
            # # Process the cleaned_data
            # prefix = request.POST['prefix']
            # first_name = request.POST['first_name']
            # last_name = request.POST['last_name']
            # date_of_birth = request.POST['date_of_birth']
            # gender = request.POST['gender']
            # home_address = request.POST['home_address']
            # national_id = request.POST['national_id']
            # phone_number = request.POST['phone_number']
            # email_address = request.POST['email_address']
            # purpose_of_visit = request.POST['purpose_of_visit']
            # description_of_the_condition = request.POST['description_of_the_condition']
            # prescription = request.POST['prescription']
            # current_temperature = request.POST['current_temperature']
            # blood_type = request.POST['blood_type']
            # current_medication = request.POST['current_medication']
            # body_mass = request.POST['body_mass']
            # allergies = request.POST['allergies']
            # employment_status = request.POST['employment_status']
            # consulted_doctor = request.POST['consulted_doctor']
            # marital_status = request.POST['marital_status']
            # medical_aid_group = request.POST['medical_aid_group']
            # date_of_visit = request.POST['date_of_visit']

            # patient_obj = Patient(prefix=prefix, first_name=first_name, last_name=last_name,date_of_birth=date_of_birth, gender=gender, home_address=home_address, national_id=national_id, phone_number=phone_number, email_address=email_address, purpose_of_visit=purpose_of_visit, description_of_the_condition=description_of_the_condition, prescription=prescription,current_temperature=current_temperature, blood_type=blood_type, current_medication=current_medication, body_mass=body_mass, allergies=allergies, employment_status=employment_status, consulted_doctor=consulted_doctor, marital_status=marital_status, medical_aid_group=medical_aid_group, date_of_visit=date_of_visit)
            # patient_obj.save()
            # print('Data saved successfully')
            form.save()
            return HttpResponseRedirect('/patients/')
    
    else:
        form = PatientModelForm()

    context = {
        'form': form, 
        'title': "Add New Patient"
    }

    return render(request, 'patients/form.html', context)

# A function to view all patients in the database
def view_all(request):
    template_name = 'view_patients.html'
    patients = Patient.objects.all()
    paginator = Paginator(patients, 30)
    if request.method == 'GET':
        page = request.GET.get('page')
    patients = paginator.get_page(page)

    context = {
        'title': 'All Patients', 
        'patients': patients
        }

    return render(request, 'patients/view_patients.html', context)

# A function to to view details of any patient selected, they're selected using the unique id
def patient_info(request, id):
    template_name = 'detail_patient.html'
    patient = Patient.objects.get(id=id)
   
    context = {
        'title': 'Patient Information',
        'patient': patient}

    return render(request, 'patients/detail_patient.html', context)

# A function used to see if there are any reports generated by the system
def get_reports(request):
    template_name = "reports.html"
    reports = Patient.objects.all()
    alert_list = [
        "Flu",
        "Cholera",
        "Waterborne",
        "Rubella"
    ]
    
    # if reports in alert_list:
    paginator = Paginator(reports, 30)
    if request.method == 'GET':
        page_requested = request.GET.get('page')
    reports = paginator.get_page(page_requested)    

    context = {
        'title' : 'Reports',
        'report' : reports
    }

    return render(request, 'patients/reports.html', context)
