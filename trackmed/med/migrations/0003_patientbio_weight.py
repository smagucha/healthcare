# Generated by Django 4.1 on 2022-08-25 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0002_remove_patientbio_age_patientbio_doe'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientbio',
            name='weight',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
