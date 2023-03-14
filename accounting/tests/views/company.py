from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import pdb # for debugging


from accounting.models import Company

class CompanyViewSetTest(APITestCase):
    def setUp(self):
      self.url = reverse('company-list')

    def test_create(self):
        data = { 'name': 'test', 'tax_refered': 'test', 'password': 'test'}
        """
        Test that we can create a new Company object using the API
        """
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
