# Generated by Django 4.1 on 2022-09-17 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0005_alter_healthdata_options_alter_patientbio_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='healthdata',
            name='user',
        ),
        migrations.RemoveField(
            model_name='medication',
            name='user',
        ),
        migrations.DeleteModel(
            name='PatientBio',
        ),
        migrations.DeleteModel(
            name='HealthData',
        ),
        migrations.DeleteModel(
            name='Medication',
        ),
    ]
