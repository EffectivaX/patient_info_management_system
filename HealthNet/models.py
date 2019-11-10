from django.db import models
from datetime import datetime
# from django.urls import reverse
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

class Doctor(models.Model):
    prefix = models.CharField(max_length=6, default='Dr')
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    qualification = models.CharField(max_length=60)
    specialty = models.CharField(max_length=60)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete = models.PROTECT)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name_plural = 'Doctors'

class Patient(models.Model):
    prefix = models.CharField(max_length=10, blank=True, choices=PREFIX_CHOICES)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=12, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    home_address = models.CharField(max_length=255)
    national_id = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    email_address = models.EmailField(blank=True)
    purpose_of_visit = models.CharField(max_length=255)
    description_of_the_condition = models.TextField(blank=True)
    prescription = models.CharField(max_length=255)
    current_temperature = models.CharField(max_length=255, blank=True)
    blood_type = models.CharField(max_length=255, choices=BLOOD_TYPE_CHOICES, blank=True)
    current_medication = models.CharField(max_length=255)
    body_mass = models.CharField(max_length=255, blank=True)
    allergies = models.CharField(max_length=255, blank=True)
    consulted_doctor = models.ForeignKey('Doctor', related_name="doctor", on_delete=models.PROTECT)
    employment_status = models.CharField(max_length=20)
    marital_status = models.CharField(max_length=20, choices=MARITAL_CHOICES)
    medical_aid_group = models.CharField(max_length=255, choices=INSURANCES)
    date_of_visit = models.DateField(default=datetime.now)
    created_at = models.DateTimeField(auto_now=True)
    # slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name_plural = "Patients"
        # ordering = ("-last_name",)

class HospitalStaff(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    identification_id = models.CharField(max_length=60, unique=True)
    qualification = models.CharField(max_length=60)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete = models.PROTECT)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name_plural = "Authorised Personnel"

class MedicalRecords(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=12, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    physical_address = models.CharField(max_length=255)
    chronic_disease = models.BooleanField()
    national_id = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    email_address = models.EmailField()
    blood_type = models.CharField(max_length=255, choices=BLOOD_TYPE_CHOICES)
    allergies = models.CharField(max_length=255)
    marital_status = models.CharField(max_length=20, choices=MARITAL_CHOICES)
    medical_aid_group = models.CharField(max_length=255, choices=INSURANCES)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name_plural = "Medical Records"

class Contact(models.Model):
    CATEGORY_CHOICE = [
        ('question', 'Question'),
        ('suggestion', 'Suggestion'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICE)
    message = models.TextField()

    def __str__(self):
        return self.name
