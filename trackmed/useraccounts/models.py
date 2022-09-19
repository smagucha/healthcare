from django.db import models
from django.contrib.auth.models import Group, Permission
from med.models import PatientBio, HealthData, Medication


doctor, created = Group.objects.get_or_create(name="doctor")
patients, created = Group.objects.get_or_create(name="patients")
administer, created = Group.objects.get_or_create(name="administer")

add_post_permission = Permission.objects.get(name="Can add health data")
view_health_data = Permission.objects.get(name="Can view health data")
change_health_data = Permission.objects.get(name="Can change health data")
delete_health_data = Permission.objects.get(name="Can delete health data")

add_medication = Permission.objects.get(name="Can add medication")
view_medication = Permission.objects.get(name="Can view medication")
change_medication = Permission.objects.get(name="Can change medication")
delete_medication = Permission.objects.get(name="Can delete medication")


add_patient = Permission.objects.get(name="Can add patient bio")
view_patient = Permission.objects.get(name="Can view patient bio")
change_patient = Permission.objects.get(name="Can change patient bio")
delete_patient = Permission.objects.get(name="Can delete patient bio")

# all_permission = Permission.objects.all()
# administer.permissions.add(all_permission)
doctor.permissions.add(
    add_post_permission,
    change_health_data,
    delete_health_data,
    view_medication,
    add_medication,
    change_medication,
    delete_medication,
    view_patient,
)

patients.permissions.add(
    view_health_data, add_patient, view_patient, change_patient, view_medication
)
