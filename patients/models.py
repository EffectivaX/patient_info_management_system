from django.db import models
from django.forms import ModelForm
from datetime import datetime
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

PREFIX_CHOICES = [
('MR', 'Mr.'),
('MRS', 'Mrs.'),
('MS', 'Ms.'),
]

GENDER_CHOICES = [
    ('MALE', 'Male'),
    ('FEMALE', 'Female')
]

BLOOD_TYPE_CHOICES = [
    ('O+', 'o+'),
    ('O-', 'o-'),
    ('AB', 'ab'),
    ('A', 'a'),
    ('B', 'b')
]


class Patient(models.Model):
    prefix = models.CharField(max_length=10, choices=PREFIX_CHOICES)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender= models.CharField(default='', max_length=12, choices=GENDER_CHOICES) 
    date_of_birth = models.DateField(default=False)
    home_address = models.CharField(default='', max_length=255)
    national_id = models.CharField(default='', max_length=30)
    phone_number = models.CharField(max_length=30)
    email_addr = models.EmailField(default=False)
    purpose_of_visit = models.CharField(max_length=255)
    description_of_condition = models.TextField(default='')
    prescription = models.CharField(max_length=255)
    curr_temp = models.CharField(max_length=255)
    blood_group = models.CharField(max_length=255, choices=BLOOD_TYPE_CHOICES)
    current_med = models.CharField(max_length=255)
    body_mass = models.CharField(max_length=255)
    allergies = models.CharField(max_length=255)
    consulted_dr = models.CharField(max_length=255)
    employment_status = models.CharField(max_length=20)
    marital_status = models.CharField(max_length=20)
    medical_aid_group = models.CharField(max_length=255)
    date_of_visit = models.DateTimeField(default=datetime.now())
    slug = models.SlugField(default='', blank=True, unique=True)
    created_at = models.DateTimeField(auto_now=True)

    def save(self):
        self.slug = slugify(self.first_name) + slugify(self.last_name)
        super(Patient, self).save()

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name_plural = "Patients"
        ordering = ("-last_name",)

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'date_of_birth']                 

