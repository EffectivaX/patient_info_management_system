from django import forms
from datetime import datetime
from .models import Patient, Doctor
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
# from django.core import validators
# from django.core.exceptions import ValidationError
# from django.utils.translation import ugettext_lazy as _


PREFIX_CHOICES = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
    ('PROF', 'Prof.'),
    ('DR', 'Dr.'),
    ('REV', 'Rev.'),
]

GENDER_CHOICES = [
    ('MALE', 'Male'),
    ('FEMALE', 'Female')
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
    ('masca', "MASCA"),
    ('nust medical aid', "NUST Medical AID"),
    ('humana', "Humana"),
    ('premier', "Premier Services"),
    ('psmas', "PSMAS"),
    ('emergency24', "Emergency 24"),
    ('EA', "Emblem Healthcare"),
    ('zimaid', "ZimAid"),
    ('KP', "Kaiser Permanente"),
    ('WP', "Wellpoint"),
)

MARITAL_CHOICES = [
        ('N/A', 'Not Applicable'),
        ('ENGAGED', 'Engaged'),
        ('SINGLE', 'Single'),
        ('DIVORCED', 'Divorced'),
        ('SEPARATED', 'Separated'),
        ('MARRIED', 'Married'),
    ]

EMPLOYMET_STATUS = [
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


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'prefix',
            'first_name',
            'last_name',
            'date_of_birth',
            'gender',
            'home_address',
            'phone_number',
            'national_id',
            'email_address',
            'purpose_of_visit',
            'description_of_the_condition',
            'prescription',
            'current_temperature',
            'blood_type',
            'current_medication',
            'body_mass',
            'allergies',
            'employment_status',
            'consulted_doctor',
            'marital_status',
            'medical_aid_group',
            'date_of_visit',
            Submit('submit', 'Submit', css_class='btn waves-effect hoverable green lighten-1 center')
            # Reset('reset', 'Reset', css_class='btn-danger')
        )

class DateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )

class PatientForm(forms.Form):
    prefix = forms.CharField(widget=forms.Select(choices=PREFIX_CHOICES, attrs={
        'class' : 'form-group col-md-2'
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'First Name',
        'class': 'form-group col-md-4'
        }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Last Name',
        'class': 'form-group col-md-4'
        }))
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day"
        ),
        attrs={
            'class' : 'form-group date col-md-4'
        }))
    gender = forms.CharField(widget=forms.Select(choices=GENDER_CHOICES, attrs={
        'class' : 'form-group col-md-4'
    }))
    home_address = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control col-md-8'
    }))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'col-md-4'
    }))
    national_id = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-group col-md-4'
    }))
    email_address = forms.EmailField(widget=forms.EmailInput(attrs={
        'class' : 'form-group col-md-6'
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
    blood_type = forms.CharField(widget=forms.Select(choices=BLOOD_TYPE_CHOICES, attrs={
        'class' : 'form-group col-md-4'
    }))
    current_medication = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-group col-md-6'
    }))
    body_mass = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-group col-md-4'
    }))
    allergies = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-group col-md-6'
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
    date_of_visit = forms.DateField(widget=forms.SelectDateWidget(attrs={
        'class' : 'form-group col-md-6'
    }))


    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
