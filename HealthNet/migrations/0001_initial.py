# Generated by Django 2.2.6 on 2019-12-06 00:00

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('A+', 'A+ Type'), ('B+', 'B+ Type'), ('AB+', 'AB+ Type'), ('O+', 'O+ Type'), ('A-', 'A- Type'), ('B-', 'B- Type'), ('AB-', 'AB- Type'), ('O-', 'O- Type')], max_length=60)),
                ('slug', models.SlugField(editable=False, max_length=12, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='blood_type', to='HealthNet.BloodGroup')),
            ],
            options={
                'verbose_name_plural': 'Blood Groups',
                'ordering': ['type'],
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Messages',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Dr', max_length=6)),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('phone_number', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('picture', models.ImageField(null=True, upload_to='images/')),
                ('qualification', models.CharField(max_length=60)),
                ('gender', models.CharField(default='', max_length=7)),
                ('date_of_birth', models.DateField(default=datetime.datetime.now)),
                ('identification_id', models.CharField(default='', max_length=30, unique=True)),
                ('specialty', models.CharField(max_length=60)),
                ('join_date', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='HealthNet.Doctor')),
            ],
            options={
                'verbose_name_plural': 'Doctors',
                'ordering': ('identification_id',),
            },
        ),
        migrations.CreateModel(
            name='HospitalsAndClinics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Mpilo Central Hospital', 'Mpilo Hospital'), ('Mater Dei Hospital', 'Mater Dei'), ('United Bulawayo Hospitals', 'UBH'), ('CIMAS', 'Cimas'), ('Corporate 24', 'Corporate 24'), ('Emergency 24', 'Emergency 24'), ('Parirenyatwa General Hospital', 'Parirenyatwa Hospital'), ('Lancet House', 'Lancet House')], max_length=60)),
                ('slug', models.SlugField(editable=False, max_length=90, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='HealthNet.HospitalsAndClinics')),
            ],
            options={
                'verbose_name_plural': 'Hospitals and Clinics',
            },
        ),
        migrations.CreateModel(
            name='MedicalAidScheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Masca', 'MASCA'), ('CIMAS', 'CIMAS'), ('Liberty Health Cover', 'Liberty Blue'), ('Alliance Health', 'Alliance Health'), ('PSMAS', 'PSMAS'), ('Health International', 'Health International'), ('Fidelity', 'Fidelity Life Insurance'), ('Minerva', 'Minerva')], max_length=60)),
                ('slug', models.SlugField(editable=False, max_length=90, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='HealthNet.MedicalAidScheme')),
            ],
            options={
                'verbose_name_plural': 'Medical AID Providers',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Mr', 'MR.'), ('Mrs', 'MRS.'), ('Ms', 'MS.'), ('Prof', 'PROF.'), ('Dr', 'DR.'), ('Rev', 'REV.')], max_length=6)),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('date_of_birth', models.DateField(null=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=7)),
                ('picture', models.ImageField(null=True, upload_to='images/')),
                ('identification_id', models.CharField(default='', max_length=30, unique=True)),
                ('position', models.CharField(max_length=100)),
                ('join_date', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='HealthNet.Staff')),
            ],
            options={
                'verbose_name_plural': 'Staff',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, choices=[('Mr', 'MR.'), ('Mrs', 'MRS.'), ('Ms', 'MS.'), ('Prof', 'PROF.'), ('Dr', 'DR.'), ('Rev', 'REV.')], max_length=10)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], max_length=12)),
                ('date_of_birth', models.DateField()),
                ('home_address', models.CharField(max_length=255)),
                ('national_id', models.CharField(max_length=30, unique=True)),
                ('phone_number', models.CharField(max_length=30, unique=True)),
                ('email_address', models.EmailField(blank=True, max_length=254, unique=True)),
                ('purpose_of_visit', models.CharField(max_length=255)),
                ('description_of_the_condition', models.TextField(blank=True)),
                ('prescription', models.CharField(max_length=255)),
                ('current_temperature', models.CharField(blank=True, max_length=255)),
                ('current_medication', models.CharField(max_length=255)),
                ('body_mass', models.PositiveIntegerField()),
                ('allergies', models.CharField(blank=True, max_length=255)),
                ('employment_status', models.CharField(choices=[('Not Applicable', 'NOT APPLICABLE'), ('Employed', 'EMPLOYED'), ('Unemployed', 'UNEMPLOYED'), ('Contract Employee', 'CONTRACT EMPLOYEE'), ('Student', 'STUDENT'), ('Retired', 'RETIRED')], max_length=20)),
                ('marital_status', models.CharField(choices=[('N/A', 'Not Applicable'), ('ENGAGED', 'Engaged'), ('SINGLE', 'Single'), ('DIVORCED', 'Divorced'), ('SEPARATED', 'Separated'), ('MARRIED', 'Married')], max_length=20)),
                ('date_of_visit', models.DateField(default=datetime.datetime.now)),
                ('slug', models.SlugField(default=None, editable=False, max_length=60, unique=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('blood_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='blood', to='HealthNet.BloodGroup')),
                ('consulted_doctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='doctor', to='HealthNet.Doctor')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='hospital', to='HealthNet.HospitalsAndClinics')),
                ('medical_aid_group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='medical_aid_user', to='HealthNet.MedicalAidScheme')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Patients',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='MedicalRecords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], max_length=12)),
                ('date_of_birth', models.DateField()),
                ('physical_address', models.CharField(max_length=255)),
                ('chronic_disease', models.BooleanField()),
                ('national_id', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=30)),
                ('email_address', models.EmailField(max_length=254)),
                ('allergies', models.CharField(max_length=255)),
                ('marital_status', models.CharField(choices=[('N/A', 'Not Applicable'), ('ENGAGED', 'Engaged'), ('SINGLE', 'Single'), ('DIVORCED', 'Divorced'), ('SEPARATED', 'Separated'), ('MARRIED', 'Married')], max_length=20)),
                ('slug', models.SlugField(default=None, editable=False, max_length=60, unique=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('blood_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Blood', to='HealthNet.BloodGroup')),
                ('medical_aid_group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='medical_aid_used', to='HealthNet.MedicalAidScheme')),
            ],
            options={
                'verbose_name_plural': 'Medical Records',
            },
        ),
    ]
