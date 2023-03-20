from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from accounting.models import User


class MyObtainTokenPairViewTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('token_obtain_pair')
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_obtain_token_pair(self):
        data = {
            'username': 'testuser',
            'password': 'testpass'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
