from django.test import TestCase
from django.urls import reverse


# Create your tests here.

class SnacksTest(TestCase):
    def test_home_page_status(self):
        url = reverse('snacks')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        url = reverse('snacks')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snacks.html')

    def test_base_page_template(self):
        url = reverse('snacks')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'base.html')

    def test_details(self):
        url = reverse('snacks')
        response = self.client.get(url + '/1/')
        self.assertEqual(response.status_code, 200)

    def test_details2(self):
        url = reverse('snacks')
        response = self.client.get(url + '/1/')
        self.assertTemplateUsed(response, 'base.html')