from django.test import TestCase
from med.views import home, createpatient, updatepatient, delete_patient
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from med.models import PatientBio

class TestCalls(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='admin', password=123456)
        PatientBio.objects.create(
            user=self.user,
            full_name='sammy magucha', 
            DOE='2022-09-18', 
            gender='F',
            height= 5.3,
            weight=87
        )
        self.data = {
            'user_id':1,
            'full_name': 'sammy magucha', 
            'DOE':'2022-09-18', 
            'gender':'F',
            'height': 5.3,
            'weight':87
            }
        self.patient = PatientBio.objects.get(id=1)

    def test_home(self):
        url = reverse('home')
        resp = self.client.get(url)
        print(resp.content)
        self.assertEqual(resolve(url).func, home)

    def test_createpatient(self):
        url = reverse('createpatient')
        response = self.client.post(
            reverse('createpatient'),
            self.data
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(resolve(url).func,createpatient )

    def test_updatepatient(self):
        url = reverse('updatepatient', kwargs={'id': self.patient.id})
        response = self.client.post(
            reverse(
                'updatepatient',
                kwargs={'id': self.patient.id}
            ),
            self.data
        )
        self.assertEqual(
            response.status_code,
            302
        )
        self.assertEqual(resolve(url).func, updatepatient)

    def test_deletepatient(self):
        url = reverse('deletepatient', kwargs={'id': self.patient.pk})
        response = self.client.delete(
            reverse(
                'deletepatient', kwargs={
                    'id': self.patient.pk
                }
            ),
            self.data
        )
        self.assertEqual(response.status_code,