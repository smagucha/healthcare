from django.forms import ModelForm
from .models import *


class PatientForm(ModelForm):
    class Meta:
        model = PatientBio
        fields = "__all__"


class HealthDataForm(ModelForm):
    class Meta:
        model = HealthData
        fields = "__all__"


class DoctorMedForm(ModelForm):
    class Meta:
        model = Medication
        fields = "__all__"
