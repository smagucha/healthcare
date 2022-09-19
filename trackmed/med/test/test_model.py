from django.test import TestCase
from datetime import datetime
from med.models import PatientBio, HealthData
from django.contrib.auth.models import User


class TestPatientBioModel(TestCase):
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

    def testPatientBioModel(self):
        patient = PatientBio.objects.create(
            user=self.user,
            full_name="sammy magucha",
            DOE="2022-09-18",
            gender="F",
            height=5.3,
            weight=87,
        )
        self.assertEquals(str(patient), "sammy magucha")
        self.assertTrue(isinstance(patient, PatientBio))

    def test_user_label(self):
        field_label = PatientBio._meta.get_field("user").verbose_name
        self.assertEqual(field_label, "user")

    def test_full_name_label(self):
        field_label = PatientBio._meta.get_field("full_name").verbose_name
        self.assertEqual(field_label, "full name")
        self.assertIsInstance(self.patient.full_name, str)

    def test_DOE_label(self):
        field_label = PatientBio._meta.get_field("DOE").verbose_name
        self.assertEqual(field_label, "DOE")

    def test_gender_label(self):
        field_label = PatientBio._meta.get_field("gender").verbose_name
        self.assertEqual(field_label, "gender")

    def test_location_label(self):
        field_label = PatientBio._meta.get_field("location").verbose_name
        self.assertEqual(field_label, "location")

    def test_height_label(self):
        field_label = PatientBio._meta.get_field("height").verbose_name
        self.assertEqual(field_label, "height")

    def test_weight_label(self):
        field_label = PatientBio._meta.get_field("weight").verbose_name
        self.assertEqual(field_label, "weight")


class TestPatientBioModel(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="admin", password=123456)
        HealthData.objects.create(
            user=self.user,
            ailments="Malaria",
            history_of_ailment="No history",
            previous_tests="no tests",
        )

        self.health = HealthData.objects.get(id=1)

    def test_PatientBioModel(self):
        health = HealthData.objects.create(
            user=self.user,
            ailments="Malaria",
            history_of_ailment="No history",
            previous_tests="no tests",
        )
        self.assertTrue(isinstance(health, HealthData))
