from django.test import TestCase
from django.urls import reverse, resolve
from med.views import home

class UrlTest(TestCase):

    def testhome(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('home'))
        self.assertRedirects(response, '/accounts/login/?next=/')