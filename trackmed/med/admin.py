from django.contrib import admin

from .models import *

admin.site.register(PatientBio)
admin.site.register(HealthData)
admin.site.register(Medication)
