from django.db import models

# Create your models here.


class Doctor(models.Model):
    prefix = models.CharField(max_length=6, default='Dr')
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    qualification = models.CharField(max_length=60)
    specialty = models.CharField(max_length=60)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name_plural = 'Doctors'
