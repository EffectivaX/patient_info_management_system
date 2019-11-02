from django.db import models
from datetime import datetime
from django.urls import reverse
from django.utils.text import slugify
from django.forms import ModelForm

# Create your models here.

PREFIX_CHOICES = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
]

GENDER_CHOICES = [('MALE', 'Male'), ('FEMALE', 'Female')]

BLOOD_TYPE_CHOICES = [('O+', 'o+'), ('O-', 'o-'), ('AB', 'ab'), ('A', 'a'),
                      ('B', 'b')]


class Patient(models.Model):
    prefix = models.CharField(max_length=10, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=12)
    date_of_birth = models.DateField(default=datetime.now)
    home_address = models.CharField(default='', max_length=255)
    national_id = models.CharField(default='', max_length=30)
    phone_number = models.CharField(max_length=30)
    email_address = models.EmailField()
    purpose_of_visit = models.CharField(max_length=255)
    description_of_the_condition = models.TextField()
    prescription = models.CharField(max_length=255)
    current_temperature = models.CharField(max_length=255)
    blood_type = models.CharField(max_length=255)
    current_medication = models.CharField(max_length=255)
    body_mass = models.CharField(max_length=255)
    allergies = models.CharField(max_length=255)
    consulted_doctor = models.CharField(max_length=255)
    employment_status = models.CharField(max_length=20)
    marital_status = models.CharField(max_length=20)
    medical_aid_group = models.CharField(max_length=255)
    date_of_visit = models.DateField(default=datetime.now)
    slug = models.SlugField(blank=True, unique=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name #'{0} {1}'.format(self.first_name, self.last_name)

    def save(self):
        # self.slug = slugify(self.first_name, self.last_name)
        super(Patient, self).save()    

    class Meta:
        verbose_name_plural = "Patients"
        # ordering = ("-last_name",)

# class PatientForm(ModelForm):
#     class Meta:
#         model = Patient
#         fields = '__all__'
