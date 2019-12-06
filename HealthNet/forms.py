from django import forms
from django.forms import ModelForm
# from datetime import datetime
from .models import Patient, Doctor, Contact, Staff, HospitalsAndClinics, MedicalAidScheme, BloodGroup
from django.conf import settings
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Submit

PREFIX_CHOICES = [
    ('Mr', 'Mr.'),
    ('Mrs', 'Mrs.'),
    ('Ms', 'Ms.'),
    ('Prof', 'Prof.'),
    ('Dr', 'Dr.'),
    ('Rev', 'Rev.'),
]

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female')
]

MARITAL_CHOICES = [
        ('Not Available', 'Not Available'),
        ('Engaged', 'Engaged'),
        ('Single', 'Single'),
        ('Divorced', 'Divorced'),
        ('Separated', 'Separated'),
        ('Married', 'Married'),
    ]

EMPLOYMET_STATUS = [
        ('Not Applicable', 'NOT APPLICABLE'),
        ('Employed', 'EMPLOYED'),
        ('Unemployed', 'UNEMPLOYED'),
        ('Contract Employee', 'CONTRACT EMPLOYEE'),
        ('Student', 'STUDENT'),
        ('Retired', 'RETIRED'),
    ]

class PatientModelForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        exclude = ['slug']

class DoctorModelForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

class StaffModelForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'

class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'



class PatientForm(forms.Form):
    title = forms.CharField(widget=forms.Select(choices=PREFIX_CHOICES, attrs={
        'class' : 'form-group col-md-2'
    }))

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-row col-md-4'
    }))

    middle_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-row col-md-4'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Last Name',
        'class': 'form-row col-md-4'
    }))

    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={
        'class' : 'form-row col-md-4',
        'placeholder' : 'YYYY-MM-DD'
    }))

    gender = forms.CharField(widget=forms.Select(choices=GENDER_CHOICES, attrs={
        'class' : 'form-row col-md-4'
    }))

    home_address = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-row col-md-6'
    }))

    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-row col-md-4'
    }))

    national_id = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-row col-md-4',
        'placeholder' : '02-1234567X30'
    }))

    email_address = forms.EmailField(required=False,widget=forms.EmailInput(attrs={
        'class' : 'form-row col-md-6',
    }))

    purpose_of_visit =forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-group col-md-6'
    }))

    description_of_the_condition = forms.CharField(widget=forms.Textarea(attrs={
        'class' : 'form-group col-md-6'
    }))

    prescription = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-group col-md-6'
    }))

    current_temperature = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-group col-md-3'
    }))

    blood_type = forms.ModelChoiceField(queryset=BloodGroup.objects.all(), required=False, widget=forms.Select(attrs={
        'class' : 'form-group col-md-4'
    }))

    current_medication = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-group col-md-6',
    }))

    body_mass = forms.IntegerField(widget=forms.TextInput(attrs={
        'class' : 'form-group col-md-4',
    }))

    allergies = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-group col-md-6',
    }))

    employment_status = forms.CharField(widget=forms.Select(choices=EMPLOYMET_STATUS, attrs={
        'class' : 'form-group col-md-6'
    }))

    consulted_doctor = forms.ModelChoiceField(queryset=Doctor.objects.all(), widget=forms.Select(attrs={
        'class' : 'form-group col-md-6'
    }))
    hospital = forms.ModelChoiceField(queryset=HospitalsAndClinics.objects.all(), widget=forms.Select(attrs={
        'class' : 'form-group col-md-6'
    }))

    marital_status = forms.CharField(widget=forms.Select(choices=MARITAL_CHOICES, attrs={
        'class' : 'form-group col-md-4'
    }))

    medical_aid_group = forms.ModelChoiceField(queryset=MedicalAidScheme.objects.all(), widget=forms.Select(attrs={
        'class' : 'form-group col-md-6'
    }))

    consultation_fee = forms.DecimalField(max_digits=10, decimal_places=2, localize=True, widget=forms.TextInput(attrs={
        'class' : 'form-group col-md-4'
    }))

    date_of_visit = forms.DateField(widget=forms.TextInput(attrs={
        'class' : 'form-row col-md-4',
        'placeholder' : 'YYYY-MM-DD'
    }))


    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)

class DoctorForm(forms.Form):
    PREFIX_LOCAL = [
        ('Dr', 'Dr')
    ]
    title = forms.CharField(widget=forms.Select(choices=PREFIX_LOCAL, attrs={
        'class' : 'form-group col-md-2'
    }))

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'First Name',
        'class': 'form-row col-md-4'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Last Name',
        'class': 'form-row col-md-4'
    }))

    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={
        'class' : 'form-row col-md-4',
        'placeholder' : 'YYYY-MM-DD'
    }))

    gender = forms.CharField(widget=forms.Select(choices=GENDER_CHOICES, attrs={
        'class' : 'form-row col-md-4'
    }))

    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-row col-md-4'
    }))

    picture = forms.FileField()

    Email = forms.EmailField(required=False,widget=forms.EmailInput(attrs={
        'class' : 'form-row col-md-6',
        'placeholder' : 'name@example.com'
    }))

    identification_id = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-row col-md-4'
    }))

    # picture = forms.FileField()

    qualification = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-group col-md-4'
    }))

    specialty = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-group col-md-4'
    }))

    join_date = forms.DateField(widget=forms.TextInput(attrs={
        'class' : 'form-row col-md-4',
        'placeholder' : 'YYYY-MM-DD'
    }))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class StaffForm(forms.Form):
    title = forms.CharField(widget=forms.Select(choices=PREFIX_CHOICES, attrs={
        'class' : 'form-group col-md-2'
    }))

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'First Name',
        'class': 'form-row col-md-4'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Last Name',
        'class': 'form-row col-md-4'
    }))

    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={
        'class' : 'form-row col-md-4',
        'placeholder' : 'YYYY-MM-DD'
    }))

    gender = forms.CharField(widget=forms.Select(choices=GENDER_CHOICES, attrs={
        'class' : 'form-row col-md-4'
    }))

    picture = forms.FileField()

    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-row col-md-4'
    }))

    Email = forms.EmailField(required=False,widget=forms.EmailInput(attrs={
        'class' : 'form-row col-md-4',
        'placeholder' : 'example@gmail.com'
    }))

    identification_id = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-row col-md-4'
    }))

    position = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-row col-md-4'
    }))

    join_date = forms.DateField(widget=forms.TextInput(attrs={
        'class' : 'form-row col-md-4',
        'placeholder' : 'YYYY-MM-DD'
    }))


    def __init__(self, *args, **kwargs):
        super(StaffForm, self).__init__(*args, **kwargs)


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-row col-md-4'
    }))
    email = forms.EmailField(label='E-Mail', widget=forms.TextInput(attrs={
        'class' : 'form-row col-md-4'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class' : 'form-row col-md-6'
    }))

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
