from django.db import models
impport datetime
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Patient(models.Model):
    prefix = models.CharField(max_length=10)
    first_name = models.CharField(max_length=255, default=False)
    last_name = models.CharField(max_length=255, default=False)
    date_of_birth = models.DateField(default=False)
    home_addr = models.CharField(default=False, max_length=255)
    national_id = models.CharField(default=False, max_length=30)
    phone_number = models.CharField(max_length=30, default=False)
    email_addr = models.EmailField(default=False)
    purpose_of_visit = models.CharField(default=False, max_length=255)
    prescription = models.CharField(default=False, max_length=255)
    curr_temp = models.CharField(default=False, max_length=255)
    blood_group = models.CharField(default=False, max_length=255)
    current_med = models.CharField(default=False, max_length=255)
    body_mass = models.CharField(default=False, max_length=255)
    allergies = models.CharField(default=False, max_length=255)
    consulted_dr = models.CharField(default=False, max_length=255)
    employment_status = models.CharField(max_length=20)
    marital_status = models.CharField(max_length=20)
    medical_aid_group = models.CharField(max_length=255)
    date_of_visit = models.DateTimeField(default=datetime.now)
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

