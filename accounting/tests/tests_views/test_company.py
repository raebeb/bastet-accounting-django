from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .test_utils import CustomAPITestCase
from accounting.models import Company

class CompanyViewSetTest(CustomAPITestCase):
    def setUp(self):
      super().setUp()
      self.url = reverse('company-list')

    def test_create(self):
        data = { 'name': 'test', 'tax_refered': 'test', 'password': 'test'}
        """
        Test that we can create a new Company object using the API
        """

        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Company.objects.count(), 1)
        self.assertEqual(Company.objects.get().organization, self.organization)

