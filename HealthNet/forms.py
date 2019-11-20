from django import forms
from datetime import datetime
from .models import Patient, Doctor, Contact, Staff
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
# from django.core import validators
# from django.core.exceptions import ValidationError
# from django.utils.translation import ugettext_lazy as _


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


BLOOD_TYPE_CHOICES = (
    ('A+', 'A+ Type'),
    ('B+', 'B+ Type'),
    ('AB+', 'AB+ Type'),
    ('O+', 'O+ Type'),
    ('A-', 'A- Type'),
    ('B-', 'B- Type'),
    ('AB-', 'AB- Type'),
    ('O-', 'O- Type'),
)

INSURANCES = (
    ('Not Applicable', "N/A"),
    ('Masca', "MASCA"),
    ('NUST Medical AID', "NUST Medical AID"),
    ('Humana', "Humana"),
    ('Premier', "Premier Services"),
    ('PSMAS', "PSMAS"),
    ('Emergency 24', "Emergency 24"),
    ('EA', "Emblem Healthcare"),
    ('zimaid', "ZimAid"),
    ('KP', "Kaiser Permanente"),
    ('WP', "Wellpoint"),
)

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

# BIRTH_YEAR_CHOICES = [range()]

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

    home_address = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-row col-md-6'
    }))

    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-row col-md-4'
    }))

    national_id = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-row col-md-4',
        'placeholder' : '08-1234567X35'
    }))

    email_address = forms.EmailField(required=False,widget=forms.EmailInput(attrs={
        'class' : 'form-row col-md-6',
        'placeholder' : 'example@gmail.com'
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

    blood_type = forms.CharField(required=False,widget=forms.Select(choices=BLOOD_TYPE_CHOICES, attrs={
        'class' : 'form-group col-md-4'
    }))

    current_medication = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-group col-md-6',
        'placeholder' : 'Morphin'
    }))

    body_mass = forms.IntegerField(widget=forms.TextInput(attrs={
        'class' : 'form-group col-md-4',
        'placeholder' : '60kg'
    }))

    allergies = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-group col-md-6',
        'placeholder' : 'chicken nuggets'
    }))

    employment_status = forms.CharField(widget=forms.Select(choices=EMPLOYMET_STATUS, attrs={
        'class' : 'form-group col-md-6'
    }))

    consulted_doctor = forms.ModelChoiceField(queryset=Doctor.objects.all(), widget=forms.Select(attrs={
        'class' : 'form-group col-md-6'
    }))

    marital_status = forms.CharField(widget=forms.Select(choices=MARITAL_CHOICES, attrs={
        'class' : 'form-group col-md-4'
    }))

    medical_aid_group = forms.CharField(widget=forms.Select(choices=INSURANCES, attrs={
        'class' : 'form-group col-md-6'
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

    Email = forms.EmailField(required=False,widget=forms.EmailInput(attrs={
        'class' : 'form-row col-md-6',
        'placeholder' : 'example@gmail.com'
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
