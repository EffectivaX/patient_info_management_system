from django.forms import ModelForm
from datetime import datetime
from .models import Patient
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.core import validators
from django.core.exceptions import ValidationError
# from django.utils.translation import ugettext_lazy as _

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"

    
    def clean(self):
        data = super(PatientForm, self).clean()
        
        prefix = cleaned_data.get('prefix')
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        gender = cleaned_data.get('gender')
        date_of_birth = cleaned_data.get('date_of_birth')
        home_address = cleaned_data.get('home_address')
        national_id = cleaned_data.get('national_id')
        phone_number = cleaned_data.get('phone_number')
        email_address = cleaned_data.get('email_address')
        purpose_of_visit = cleaned_data.get('purpose_of_visit')
        description_of_the_condition = cleaned_data.get('description_of_the_condition')
        prescription = cleaned_data.get('prescription')
        current_temperature = cleaned_data.get('current_temperature')
        blood_type = cleaned_data.get('blood_type')
        current_medication = cleaned_data.get('current_medication')
        body_mass = cleaned_data.get('body_mass')
        allergies = cleaned_data.get('allergies')
        consulted_doctor = cleaned_data.get('consulted_doctor')
        employment_status = cleaned_data.get('employment_status')
        marital_status = cleaned_data.get('marital_status')
        medical_aid_group = cleaned_data.get('medical_aid_group')
        date_of_visit = cleaned_data.get('date_of_visit')

        if not first_name and not last_name and not gender and not date_of_birth and not national_id and not phone_number and not email_address and not purpose_of_visit and not description_of_the_condition and not prescription and not current_medication and not blood_type and not current_medication and not body_mass and not allergies and not consulted_doctor and not employment_status and not marital_status and not medical_aid_group and not date_of_visit:

            raise forms.validationError("You cannot leave blanks!")



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
            Submit('submit', 'Submit', css_class='btn waves-effect hoverable green lighten-1 center')
            # Reset('reset', 'Reset', css_class='btn-danger')
        )


