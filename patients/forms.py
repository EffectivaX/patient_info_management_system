from django.forms import ModelForm
from django import forms
from datetime import datetime
from .models import Patient
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.core import validators
from django.core.exceptions import ValidationError
# from django.utils.translation import ugettext_lazy as _

class PatientModelForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"
        exclude = ['slug']


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
            'national_id',
            'phone_number',
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
            # Submit('submit', 'Submit', css_class='btn waves-effect hoverable green lighten-1 center')
            # Reset('reset', 'Reset', css_class='btn-danger')
        )

class PatientForm(forms.Form):
    prefix = forms.CharField(max_length=6)
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    date_of_birth = forms.DateField()
    gender = forms.CharField(max_length=6)
    home_address = forms.CharField(max_length=255)
    national_id = forms.CharField(max_length=30)
    phone_number = forms.CharField(max_length=30)
    email_address = forms.EmailField()
    purpose_of_visit = forms.CharField(max_length=255)
    description_of_the_condition = forms.CharField(widget=forms.Textarea)
    prescription = forms.CharField(max_length=255)
    current_temperature = forms.IntegerField()
    blood_type = forms.CharField(max_length=255)
    current_medication = forms.CharField(max_length=255)
    body_mass = forms.IntegerField()
    allergies = forms.CharField(max_length=255)
    employment_status = forms.CharField(max_length=20)
    consulted_doctor = forms.CharField(max_length=255)
    marital_status = forms.CharField(max_length=20)
    medical_aid_group = forms.CharField(max_length=255)
    date_of_visit = forms.DateField()



