from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
# from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django import forms
from django.conf import settings
from django.contrib import messages
# Create your views here.
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .models import Patient, Doctor, Staff, Contact
from .forms import PatientForm, ContactForm, DoctorForm, StaffForm, ContactModelForm
# from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
# from django.views.generic.edit import DeleteView

# login_required_m = method_decorator(login_required)

@login_required
def index(request):
    context = {
        'title': 'HealthNet Dashboard',
        'project_name' : 'ProMed HealthNet Inc',
        'creator' : 'Andile XeroxZen',
        'purpose' : 'Patient Information Management System'
    }

    return render(request, 'HealthNet/index.html', context)

# A function to add new patient to the database
# This form uses the PatientModelForm()
@login_required
def patient_form(request):
    form = PatientForm()
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            # Process the cleaned_data
            patient = Patient.objects.create(
                title = form.cleaned_data.get('title'),
                first_name = form.cleaned_data.get('first_name'),
                last_name = form.cleaned_data.get('last_name'),
                date_of_birth = form.cleaned_data.get('date_of_birth'),
                gender = form.cleaned_data.get('gender'),
                home_address = form.cleaned_data.get('home_address'),
                national_id = form.cleaned_data.get('national_id'),
                phone_number = form.cleaned_data.get('phone_number'),
                email_address = form.cleaned_data.get('email_address'),
                purpose_of_visit = form.cleaned_data.get('purpose_of_visit'),
                description_of_the_condition = form.cleaned_data.get('description_of_the_condition'),
                prescription = form.cleaned_data.get('prescription'),
                current_temperature = form.cleaned_data.get('current_temperature'),
                blood_type = form.cleaned_data.get('blood_type'),
                current_medication = form.cleaned_data.get('current_medication'),
                body_mass = form.cleaned_data.get('body_mass'),
                allergies = form.cleaned_data.get('allergies'),
                employment_status = form.cleaned_data.get('employment_status'),
                consulted_doctor = form.cleaned_data.get('consulted_doctor'),
                hospital = form.cleaned_data.get('hospital'),
                marital_status = form.cleaned_data.get('marital_status'),
                medical_aid_group = form.cleaned_data.get('medical_aid_group'),
                date_of_visit = form.cleaned_data.get('date_of_visit'),
            )

            patient.user = request.user
            patient.save()
            messages.success(request, 'Patient added successfully!', extra_tags='alert')
            return HttpResponseRedirect('/HealthNet/patients/view_all/')
        else:
            messages.warning(request, 'Please correct the error identified...', extra_tags='alerts')

    else:
        form = PatientForm()

    context = {
        'form': form,
        'button' : 'Add Patient',
        'title': "Add New Patient",
        'project_name' : 'ProMed HealthNet Inc',
        'creator' : 'Andile XeroxZen',
        'purpose' : 'Patient Information Management System'
    }

    return render(request, 'HealthNet/form.html', context)

# A function for a successfull posting
# def success(request):
#      return HttpResponseRedirect('/HealthNet/success.html')

# A function to view all patients in the database
@permission_required('HealthNet.view_patients')
def view_all(request):
    # Authentication check
    template_name = 'view_patients.html'
    patients = Patient.objects.all()
    paginator = Paginator(patients, 50)
    if request.method == 'GET':
        try:
            page = request.GET.get('page')
        except Exception:
            return HttpResponseRedirect('/HealthNet/')
    patients = paginator.get_page(page)

    context = {
        'title': 'All Patients',
        'patients': patients,
        'project_name' : 'ProMed HealthNet Inc',
        'creator' : 'Andile XeroxZen',
        'purpose' : 'Patient Information Management System'
        }

    return render(request, 'HealthNet/view_patients.html', context)

# A function to to view details of any patient selected, they're selected using the unique id
@permission_required('HealthNet.see_patient')
def patient_info(request, id):
    template_name = 'detail_patient.html'
    patient = Patient.objects.get(id=id)

    context = {
        'title': 'Information',
        'patient': patient,
        'project_name' : 'ProMed HealthNet Inc',
        'creator' : 'Andile XeroxZen',
        'purpose' : 'Patient Information Management System'
    }

    return render(request, 'HealthNet/detail_patient.html', context)

# This is a function for editing a patient's Information

@login_required
def edit_patient(request, pk=None):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.user = request.user
            patient.save()
            messages.success(request, 'Patient updated successfully!', extra_tags='alert')
            return redirect('HealthNet:view_all')
    else:
        form = PatientForm(instance=patient)
    template_name = 'HealthNet/form.html'
    context = {
        'title': 'Updating Information',
        'form': form,
        'project_name' : 'ProMed HealthNet Inc',
        'button' : 'Update',
        'creator' : 'Andile XeroxZen',
        'purpose' : 'Patient Information Management System'
    }

    return render(request, template_name, context)

# This is a delete function
@login_required
def delete_patient(request, id=None):
    if request.method == 'GET' and 'DELETE' in request.GET:
        Patient.objects.filter(pk=id).delete()
        return HttpResponseRedirect(request.path)

    else:
        form = Patient()
    context = {
        'form' : form
    }
    return redirect(request, 'HealthNet/patients/view_all', context)

# A function used to see if there are any reports generated by the system
@login_required
def reports(request):
    template_name = "/HealthNet/reports.html"
    reports = Patient.objects.all()
    paginator = Paginator(reports, 60)

    if request.method == 'GET':
        try:
            page_requested = request.GET.get('page')
        except Exception:
            return HttpResponseRedict('/HealthNet/')
    reports = paginator.get_page(page_requested)

    context = {
        'title' : 'Reports',
        'reports' : reports,
        'project_name' : 'ProMed HealthNet Inc',
        'creator' : 'Andile XeroxZen',
        'purpose' : 'Patient Information Management System'
    }

    return render(request, 'HealthNet/reports.html', context)

# Fucnction Add Staff Members
@login_required
def add_staff_member(request):
    form = StaffForm()
    if request.method == 'POST':
        form = StaffForm(request.POST, request.FILES)
        if form.is_valid():
            # Process and clean the data
            staff_member = Staff.objects.create(
                title = form.cleaned_data.get('title'),
                first_name = form.cleaned_data.get('first_name'),
                last_name = form.cleaned_data.get('last_name'),
                date_of_birth = form.cleaned_data.get('date_of_birth'),
                picture = form.cleaned_data.get('picture'),
                gender = form.cleaned_data.get('gender'),
                phone_number = form.cleaned_data.get('phone_number'),
                Email = form.cleaned_data.get('Email'),
                identification_id = form.cleaned_data.get('identification_id'),
                position = form.cleaned_data.get('position'),
                join_date = form.cleaned_data.get('join_date')
            )

            staff_member.save()
            messages.success(request, 'Staff Member added successfully!', extra_tags='alert')
            return HttpResponseRedirect('/HealthNet/staff/all_members/')
        else:
            messages.warning(request, 'Staff Member failed to update!', extra_tags='alert')
    else:
        form = StaffForm()

    context = {
        'form' : form,
        'button' : 'Add Member',
        'project_name' : 'ProMed HealthNet Inc',
        'title' : 'Add New Staff Member'
    }

    return render(request, 'HealthNet/form.html', context)

# Function to edit or update a staff members
@login_required
def update_member(request, pk=None):
    member = get_object_or_404(Staff, pk=pk)
    if request.method == "POST":
        form = StaffForm(request.POST, instance=member)
        if form.is_valid():
            form.save()

        messages.success(request, 'Staff Member updated successfully!', extra_tags='alert')
        return HttpResponseRedirect('/HealthNet/staff/all_members/')

    context = {
        'title': 'Staff Member',
        'form': form,
        'project_name' : 'ProMed HealthNet Inc',
        'creator' : 'Andile XeroxZen',
        'purpose' : 'Patient Information Management System'
    }

    return render(request, 'HealthNet/form.html', context)

# Function to delete a staff member
@login_required
def delete_staff_member(request, id=None):
    item = get_object_or_404(Staff, id=id)

    if request.method == 'POST':
        form = StaffForm(request.POST, instance = item)
        if form.is_valid():
            item.delete()
            messages.info(request,'Staff Member successfully deleted!')
            return HttpResponseRedirect("/HealthNet/staff/all_members/")
    else:
        form = StaffForm(instance=item)
    context = {
        'form' : form
    }
    return redirect(request, 'HealthNet/staff/all_members/', context)

# Function to display all staff members
@login_required
def all_members(request):
    template = 'HealthNet/members.html'
    members = Staff.objects.all()
    paginator = Paginator(members, 50)
    if request.method == 'GET':
        try:
            page = request.GET.get('page')
        except Exception:
            return HttpResponseRedirect('/error/denied/')
    staff = paginator.get_page(page)

    context = {
        'title': 'Staff Members',
        'members': members,
        'project_name' : 'ProMed HealthNet Inc',
        'creator' : 'Andile XeroxZen',
        'purpose' : 'Patient Information Management System'
        }

    return render(request, template, context)

# Function to add doctors
@login_required
def add_doctor(request):
    form = DoctorForm()
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            # Process and clean the data
            doctor = Doctor.objects.create(
                title = form.cleaned_data.get('title'),
                first_name = form.cleaned_data.get('first_name'),
                last_name = form.cleaned_data.get('last_name'),
                date_of_birth = form.cleaned_data.get('date_of_birth'),
                gender = form.cleaned_data.get('gender'),
                phone_number = form.cleaned_data.get('phone_number'),
                Email = form.cleaned_data.get('Email'),
                identification_id = form.cleaned_data.get('identification_id'),
                picture = form.cleaned_data.get('picture'),
                qualification = form.cleaned_data.get('qualification'),
                specialty = form.cleaned_data.get('specialty'),
                join_date = form.cleaned_data.get('join_date')

            )

            doctor.save()
            messages.success(request, 'Doctor added successfully!', extra_tags='alert')
            return redirect('/HealthNet/staff/doctors/')
        else:
            messages.warning(request, 'Doctor could not be added!', extra_tags='alert')
    else:
        form = DoctorForm()

    context = {
        'form' : form,
        'button' : 'Submit Doctor',
        'project_name' : 'ProMed HealthNet Inc',
        'title' : 'Add New Doctor'
    }

    return render(request, 'HealthNet/form.html', context)

@login_required
def all_doctors(request):
    template = 'staff.html'
    staff = Doctor.objects.all()
    paginator = Paginator(staff, 20)
    if request.method == 'GET':
        page = request.GET.get('page')
    staff = paginator.get_page(page)

    context = {
        'title': 'All Doctors',
        'staff': staff,
        'project_name' : 'ProMed HealthNet Inc',
        'creator' : 'Andile XeroxZen',
        'purpose' : 'Patient Information Management System'
        }

    return render(request, 'HealthNet/doctors.html', context)

@login_required
def delete_doctor(request, id=None):
    item = get_object_or_404(Doctor, id=id)

    if request.method == 'POST':
        form = DoctorForm(request.POST, instance = item)
        if form.is_valid():
            item.delete()
            return HttpResponse("Patient successfully deleted")
    else:
        form = DoctorForm(instance=item)
    context = {
        'form' : form
    }
    return redirect(request, 'HealthNet/patients/view_all', context)

@login_required
def update_doctor(request, id=None):
    item = get_object_or_404(Doctor, id=id)
    form = DoctorForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        messages.success(request, 'Doctor updated successfully!', extra_tags='alert')
        return HttpResponseRedirect('/HealthNet/staff/doctors/')

    context = {
        'title': 'Update Doctor',
        'form': form,
        'project_name' : 'ProMed HealthNet Inc',
        'creator' : 'Andile XeroxZen',
        'purpose' : 'Patient Information Management System'
    }

    return render(request, 'HealthNet/form.html', context)



def contact(request):
    if request.method == 'POST':
        form = ContactForm()
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            print(email + 'sent a message')

            return HttpResponse('Message was successfully sent...')
    else:
        form = ContactForm()

    context = {
        'form' : form,
        'button' : 'Send Message',
        'project_name' : 'ProMed HealthNet Inc',
        'title' : 'Contact Us'
    }
    return render(request, 'HealthNet/form.html', context)

def contact_form(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent successfully!', extra_tags='alert')
            return HttpResponseRedirect('/HealthNet/messages/')
        else:
            messages.warning(request, 'Message not sent, try again in a bit!', extra_tags='alert')
    else:
        form = ContactModelForm()

    context = {
        'form' : form,
        'button' : 'Send Message',
        'project_name' : 'ProMed HealthNet Inc',
        'title' : 'Contact Us'
    }
    return render(request, 'HealthNet/contact_form.html', context)

def read_messages(request):
    msgs = Contact.objects.all()
    paginator = Paginator(msgs, 20)
    if request.method == 'GET':
        page = request.GET.get('page')
    msgs = paginator.get_page(page)

    context = {
        'title': 'All Messages',
        'msgs': msgs,
        'project_name' : 'ProMed HealthNet Inc',
        'creator' : 'Andile XeroxZen',
        'purpose' : 'Patient Information Management System'
        }

    return render(request, 'HealthNet/messages.html', context)
