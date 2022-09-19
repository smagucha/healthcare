from django.test import TestCase
from med.views import (
    home,
    createpatient,
    updatepatient,
    delete_patient,
    viewpatient,
    list_health_data,
    create_patient_data,
    delete_health_data,
    createmedication,
    list_medication,
    updatemedication,
    deletemedication,
    patient_view_med,
    patient_view,
)
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from med.models import PatientBio, HealthData, Medication


class TestPatient(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="admin", password=123456)
        PatientBio.objects.create(
            user=self.user,
            full_name="sammy magucha",
            DOE="2022-09-18",
            gender="F",
            height=5.3,
            weight=87,
        )
        self.data = {
            "user_id": 1,
            "full_name": "sammy magucha",
            "DOE": "2022-09-18",
            "gender": "F",
            "height": 5.3,
            "weight": 87,
        }
        self.patient = PatientBio.objects.get(id=1)

    def test_home(self):
        url = reverse("home")
        response = self.client.get(reverse("home"))
        resp = self.client.get(url)
        self.assertEqual(resolve(url).func, home)

    def test_createpatient(self):
        url = reverse("createpatient")
        response = self.client.post(url, self.data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(resolve(url).func, createpatient)

    def test_updatepatient(self):
        url = reverse("updatepatient", kwargs={"id": self.patient.id})
        response = self.client.post(url, self.data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(resolve(url).func, updatepatient)

    def test_deletepatient(self):
        url = reverse("deletepatient", kwargs={"id": self.patient.id})
        response = self.client.delete(url, self.data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(resolve(url).func, delete_patient)

    def test_viewpatient(self):
        url = reverse("viewpatient", kwargs={"id": self.patient.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(resolve(url).func, viewpatient)


class TestHealthData(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="admin", password=123456)
        self.data = {
            "user": self.user,
            "ailments": "malaria",
            "history_of_ailments": "no previous illness",
            "previous_test": "no tests",
        }
        HealthData.objects.create(
            user=self.user,
            ailments="malaria",
            history_of_ailment="no history",
            previous_tests="no tests",
        )
        self.health = HealthData.objects.get(id=1)

    def test_list_health_data(self):
        url = reverse("listhealthdata")
        response = self.client.get(url)
        self.assertEqual(resolve(url).func, list_health_data)

    def test_createhealtdata(self):
        url = reverse("createpatientdata")
        response = self.client.post(url, self.data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(resolve(url).func, create_patient_data)

    def test_delete_health_data(self):
        url = reverse("deletehealthdata", kwargs={"id": self.health.id})
        response = self.client.post(url, self.data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(resolve(url).func, delete_health_data)


class TestMedication(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="admin", password=123456)
        self.data = {
            "user": self.user,
            "medicine": "panadol",
            "days_to_take": 15,
            "schedule": " 3 x 4",
        }
        Medication.objects.create(
            user=self.user,
            medicine="panadol",
            days_to_take=15,
            schedule="3 x 5",
        )
        self.med = Medication.objects.get(id=1)

    def test_createmedication(self):
        url = reverse("createmedication")
        response = self.client.post(url, self.data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(resolve(url).func, createmedication)

    def test_list_medication(self):
        url = reverse("listmedication")
        response = self.client.get(url)
        self.assertEqual(resolve(url).func, list_medication)

    def test_updatemedication(self):
        url = reverse("updatemedication", kwargs={"id": self.med.id})
        response = self.client.delete(url, self.data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(resolve(url).func, updatemedication)

    def test_deletemedication(self):
        url = reverse("deletemedication", kwargs={"id": self.med.id})
        response = self.client.post(url, self.data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(resolve(url).func, deletemedication)

    def test_patient_view(self):
        url = reverse("patientview")
        response = self.client.get(url)
        self.assertEqual(resolve(url).func, patient_view)

    def test_patient_view_med(self):
        url = reverse("patientviewmed")
        response = self.client.get(url)
        self.assertEqual(resolve(url).func, patient_view_med)
