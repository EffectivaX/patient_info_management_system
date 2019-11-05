from django import forms
from django.forms import ModelForm
from datetime import datetime
from .models import Patient
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.core import validators
from django.core.exceptions import ValidationError
# from django.utils.translation import ugettext_lazy as _

class PatientModelForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
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



