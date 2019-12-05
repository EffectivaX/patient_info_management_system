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
        ordering = ("id",)

class HospitalsAndClinics(models.Model):
    HOSPITAL_CHOICES = [
    ('Mpilo Central Hospital', 'Mpilo Hospital'),
    ('Mater Dei Hospital', 'Mater Dei'),
    ('United Bulawayo Hospitals', 'UBH'),
    ('CIMAS', 'Cimas'),
    ('Corporate 24', 'Corporate 24'),
    ('Emergency 24', 'Emergency 24'),
    ('Parirenyatwa General Hospital', 'Parirenyatwa Hospital'),
    ('Lancet House', 'Lancet House'),
    ]

    name = models.CharField(max_length=60, choices=HOSPITAL_CHOICES)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.PROTECT)
    slug = models.SlugField(max_length=90, unique=True, editable=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)    

    class Meta:
        verbose_name_plural = 'Hospitals and Clinics'


class MedicalAidScheme(models.Model):
    INSURANCES = [
        ('Masca', "MASCA"),
        ('CIMAS', "CIMAS"),
        ('Liberty Health Cover', "Liberty Blue"),
        ('Alliance Health', "Alliance Health"),
        ('PSMAS', "PSMAS"),
        ('Health International', "Health International"),
        ('Fidelity', "Fidelity Life Insurance"),
        ('Minerva', "Minerva")
    ]

    name = models.CharField(max_length=60, choices=INSURANCES)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete = models.CASCADE)
    slug = models.SlugField(max_length=90, unique=True, editable=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("HealthNet:medical_aid", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Medical AID Providers'

# class PatientProfile(models.Model):
#     full_name = models.CharField(max_length=60)
#     member = models.CharField(max_length=60)
#     relationship_to_member = models.CharField(max_length=30)
#     gender = models.CharField(max_length=8)
#     identification = models.CharField(max_length=30)
#
#     class Meta:
#         verbose_name_plural = 'Patient Profile'
#     def __str__(self):
#         return self.full_name


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
    hospital = models.ForeignKey('HospitalsAndClinics', related_name='hospital', on_delete=models.PROTECT)
    employment_status = models.CharField(max_length=20, choices=EMPLOYMET_STATUS)
    marital_status = models.CharField(max_length=20, choices=MARITAL_CHOICES)
    # medical_aid_group = models.CharField(max_length=255, choices=INSURANCES)
    medical_aid_group = models.ForeignKey('MedicalAidScheme', related_name='medical_aid_user', on_delete=models.PROTECT)
    date_of_visit = models.DateField(default=datetime.now)
    User = settings.AUTH_USER_MODEL
    user = models.ForeignKey(User, null=True, on_delete=models.PROTECT)
    slug = models.SlugField(max_length=60, unique=True, editable=False, default=None)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return reverse("HealthNet:view_all", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        name = self.first_name + self.last_name
        self.slug = slugify(name, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Patients"
        # ordering = ("-last_name",)

# class MedicalRecords(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     gender = models.CharField(max_length=12, choices=GENDER_CHOICES)
#     date_of_birth = models.DateField()
#     physical_address = models.CharField(max_length=255)
#     chronic_disease = models.BooleanField()
#     national_id = models.CharField(max_length=30)
#     phone_number = models.CharField(max_length=30)
#     email_address = models.EmailField()
#     blood_type = models.CharField(max_length=255, choices=BLOOD_TYPE_CHOICES)
#     allergies = models.CharField(max_length=255)
#     marital_status = models.CharField(max_length=20, choices=MARITAL_CHOICES)
#     # medical_aid_group = models.ForeignKey('MedicalAidScheme', related_name='medical_aid_used', on_delete=models.PROTECT, default=None)
#     slug = models.SlugField(default=None, unique=True, max_length=60, editable=False)
#     created_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.first_name + " " + self.last_name
#
#     def save(self, *args, **kwargs):
#         value = self.first_name
#         self.slug = slugify(value, allow_unicode=True)
#         super().save(*args, **kwargs)
#
#     class Meta:
#         verbose_name_plural = "Medical Records"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'Messages'
