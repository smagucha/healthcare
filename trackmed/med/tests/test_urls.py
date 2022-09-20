from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from med.models import PatientBio, Medication, HealthData


class UrlTest(TestCase):
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
        self.patient = PatientBio.objects.get(id=1)
        Medication.objects.create(
            user=self.user,
            medicine="panadol",
            days_to_take=15,
            schedule="3 x 5",
        )
        self.med = Medication.objects.get(id=1)
        HealthData.objects.create(
            user=self.user,
            ailments="malaria",
            history_of_ailment="no history",
            previous_tests="no tests",
        )
        self.health = HealthData.objects.get(id=1)

    def testhome_url(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 302)

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse("home"))
        self.assertRedirects(response, "/accounts/login/?next=/")
        self.assertEqual(response.status_code, 302)

    def test_createpatient_url(self):
        response = self.client.get(reverse("createpatient"))
        self.assertEqual(response.status_code, 302)

    def test_updatepatient_url(self):
        response = self.client.get(
            reverse("updatepatient", kwargs={"id": self.patient.id})
        )
        self.assertEqual(response.status_code, 302)

    def test_delete_patient_url(self):
        response = self.client.get(
            reverse("deletepatient", kwargs={"id": self.patient.id})
        )
        self.assertEqual(response.status_code, 302)

    def test_createmedication_url(self):
        response = self.client.get(reverse("createmedication"))
        self.assertEqual(response.status_code, 302)

    def test_updatemedication_url(self):
        response = self.client.get(
            reverse("updatemedication", kwargs={"id": self.med.id})
        )
        self.assertEqual(response.status_code, 302)

    def test_deletemedication_url(self):
        response = self.client.get(
            reverse("deletemedication", kwargs={"id": self.med.id})
        )
        self.assertEqual(response.status_code, 302)

    def test_list_medication(self):
        response = self.client.get(reverse("listmedication"))
        self.assertEqual(response.status_code, 302)

    def test_listhealthdata(self):
        response = self.client.get(reverse("listhealthdata"))
        self.assertEqual(response.status_code, 302)

    def test_createhealtdata_url(self):
        response = self.client.get(reverse("createpatientdata"))
        self.assertEqual(response.status_code, 302)

    def test_deletehealthdata_url(self):
        response = self.client.get(
            reverse("deletehealthdata", kwargs={"id": self.health.id})
        )
        self.assertEqual(response.status_code, 302)

    def test_patient_view_url(self):
        response = self.client.get(reverse("patientview"))
        self.assertEqual(response.status_code, 302)

    def test_patient_view_med_url(self):
        response = self.client.get(reverse("patientviewmed"))
        self.assertEqual(response.status_code, 302)
