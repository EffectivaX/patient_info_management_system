from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

# Create your forms here.


class PatientRegistrationForm(forms.Form):
    prefix = forms.CharField(max_length=10)
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    date_of_birth = forms.DateTimeField()
    gender = forms.CharField()
    home_address = forms.CharField(max_length=255)
    national_id = forms.CharField(max_length=30)
    phone_number = forms.CharField(max_length=30)
    email_address = forms.EmailField()
    purpose_of_visit = forms.CharField(max_length=255)
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

    def save(self):
        self.slug = slugify(self.first_name) + slugify(self.last_name)
        super(Patient, self).save()

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self(last_name))

    class Meta:
        verbose_name_plural = "Patients"
        ordering = ("-last_name", )
        model = User

    def save(self, commit=True):
        patient = super(PatientRegistrationForm, self).save(commit=False)
        # user.set_password(self.cleaned_data['password1'])

        if commit:
            patient.save()
        return patient
