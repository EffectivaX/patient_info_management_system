from django.db import models
from datetime import datetime
from django.conf import settings
# from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
from django.conf import settings
from django.db.models.signals import post_save


def post_save_receiver(sender, instance, created, **kwargs):
    pass

post_save.connect(post_save_receiver, sender=settings.AUTH_USER_MODEL)

PREFIX_CHOICES = [
    ('Mr', 'MR.'),
    ('Mrs', 'MRS.'),
    ('Ms', 'MS.'),
    ('Prof', 'PROF.'),
    ('Dr', 'DR.'),
    ('Rev', 'REV.'),
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
    ('Masca', "MASCA"),
    ('NUST Medical Aid', "NUST Medical AID"),
    ('Humana', "Humana"),
    ('Premier', "Premier Services"),
    ('PSMAS', "PSMAS"),
    ('Emergency24', "Emergency 24"),
    ('EA', "Emblem Healthcare"),
    ('ZimAid', "ZimAid"),
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
        ('Not Applicable', 'NOT APPLICABLE'),
        ('Employed', 'EMPLOYED'),
        ('Unemployed', 'UNEMPLOYED'),
        ('Contract Employee', 'CONTRACT EMPLOYEE'),
        ('Student', 'STUDENT'),
        ('Retired', 'RETIRED'),
    ]

class Doctor(models.Model):
    title = models.CharField(max_length=6, default='Dr')
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=20)
    Email = models.EmailField()
    picture = models.ImageField(upload_to='images/', null=True, height_field=None, width_field=None, max_length=None)
    qualification = models.CharField(max_length=60)
    gender = models.CharField(max_length=7, default='')
    date_of_birth = models.DateField(default=datetime.now)
    identification_id = models.CharField(max_length=30, default='',unique=True)
    specialty = models.CharField(max_length=60)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete = models.PROTECT)
    join_date = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name_plural = 'Doctors'
        ordering = ("identification_id",)

class Staff(models.Model):
    title = models.CharField(max_length=6, choices=PREFIX_CHOICES)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    date_of_birth = models.DateField(null=True)
    phone_number = models.CharField(max_length=20)
    Email = models.EmailField()
    gender = models.CharField(max_length=7)
    picture = models.ImageField(upload_to='images/', null=True, height_field=None, width_field=None, max_length=None)
    identification_id = models.CharField(max_length=30, default='',unique=True)
    position = models.CharField(max_length=100)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete = models.PROTECT)
    join_date = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name_plural = 'Staff'
        ordering = ("identification_id",)


class Patient(models.Model):
    title = models.CharField(max_length=10, blank=True, choices=PREFIX_CHOICES)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=12, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    home_address = models.CharField(max_length=255)
    national_id = models.CharField(max_length=30, unique=True)
    phone_number = models.CharField(max_length=30, unique=True)
    email_address = models.EmailField(blank=True, unique=True)
    purpose_of_visit = models.CharField(max_length=255)
    description_of_the_condition = models.TextField(blank=True)
    prescription = models.CharField(max_length=255)
    current_temperature = models.CharField(max_length=255, blank=True)
    blood_type = models.CharField(max_length=255, choices=BLOOD_TYPE_CHOICES, blank=True)
    current_medication = models.CharField(max_length=255)
    body_mass = models.PositiveIntegerField()
    allergies = models.CharField(max_length=255, blank=True)
    consulted_doctor = models.ForeignKey('Doctor', related_name="doctor", on_delete=models.PROTECT)
    employment_status = models.CharField(max_length=20, choices=EMPLOYMET_STATUS)
    marital_status = models.CharField(max_length=20, choices=MARITAL_CHOICES)
    medical_aid_group = models.CharField(max_length=255, choices=INSURANCES)
    date_of_visit = models.DateField(default=datetime.now)
    # created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='user')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name_plural = "Patients"
        # ordering = ("-last_name",)

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
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'Messages'
