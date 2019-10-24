import datetime
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django import forms

from patients.models import Patient
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

User = get_user_model()

# Create your forms here.

PREFIX_CHOICES = [
('MR', 'Mr.'),
('MRS', 'Mrs.'),
('MS', 'Ms.'),
]


class PatientRegistrationForm(forms.Form):
    prefix = forms.CharField(max_length=6)
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    date_of_birth = forms.DateTimeField()
    gender = forms.CharField(max_length=6)
    home_address = forms.CharField(max_length=255)
    national_id = forms.CharField(max_length=30)
    phone_number = forms.CharField(max_length=30)
    email_address = forms.EmailField()
    purpose_of_visit = forms.CharField(max_length=255)
    description_of_the_condition = forms.Textarea()
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
    date_of_visit = forms.DateTimeField()
    # slug = forms.SlugField(required=True)
    # created_at = forms.DateTimeField()

    def clean_patient_registration_form(self):
        prefix = self.cleaned_data['prefix']
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        date_of_birth = self.cleaned_data['date_of_birth']
        gender = self.cleaned_data['gender']
        home_address = self.cleaned_data['home_address']
        national_id = self.cleaned_data['national_id']
        phone_number_ = self.cleaned_data['phone_number']
        email_address = self.cleaned_data['email_address']
        purpose_of_visit = self.cleaned_data['purpose_of_visit']
        description_of_the_condition = self.cleaned_data['description_of_the_condition']
        blood_type= self.cleaned_data['blood_type']
        current_medication = self.cleaned_data['current_medication']
        body_mass = self.cleaned_data['body_mass']
        alleries = self.cleaned_data['allergies']
        employment_status = self.cleaned_data['employment_status']
        consulted_doctor = self.cleaned_data['consulted_doctor']
        marital_status = self.cleaned_data['marital_status']
        medical_aid_group = self.cleaned_data['medical_aid_goup']
        date_of_visit = self.cleaned_data['date_of_visit']

    def save(self):
        self.slug = slugify(self.first_name) + slugify(self.last_name)
        super(Patient, self).save()

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self(last_name))

    class Meta:
        verbose_name_plural = "Patients"
        ordering = ("-last_name", )
        model = User

    def save(self):
        patient = super(PatientRegistrationForm, self).save(commit=False)
        # user.set_password(self.cleaned_data['password1'])

        if commit:
            patient.save()
        return patient
