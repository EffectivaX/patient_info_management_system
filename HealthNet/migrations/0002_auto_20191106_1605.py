# Generated by Django 2.2.6 on 2019-11-06 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthNet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='marital_status',
            field=models.CharField(choices=[('N/A', 'Not Applicable'), ('ENGAGED', 'Engaged'), ('SINGLE', 'Single'), ('DIVORCED', 'Divorced'), ('SEPARATED', 'Separated'), ('MARRIED', 'Married')], max_length=20),
        ),
        migrations.AlterField(
            model_name='patient',
            name='medical_aid_group',
            field=models.CharField(choices=[('Not Applicable', 'N/A'), ('masca', 'MASCA'), ('nust medical aid', 'NUST Medical AID'), ('humana', 'Humana'), ('premier', 'Premier Services'), ('psmas', 'PSMAS'), ('emergency24', 'Emergency 24'), ('EA', 'Emblem Healthcare'), ('zimaid', 'ZimAid'), ('KP', 'Kaiser Permanente'), ('WP', 'Wellpoint')], max_length=255),
        ),
    ]
