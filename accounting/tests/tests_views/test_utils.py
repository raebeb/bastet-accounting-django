from accounting.models import User
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken

from accounting.tests.factories.models.organization_factory import OrganizationFactory
from accounting.tests.factories.models.user_factory import UserFactory
from accounting.tests.factories.models.membership_factory import MembershipFactory



class CustomAPITestCase(APITestCase):
    def setUp(self):
        url = reverse('token_obtain_pair')
        organization = OrganizationFactory()
        organization.save()

        self.user = UserFactory(username='fran')
        self.user.save()
        data = {
            'username': self.user.username,
            'password': 'password'
        }
        membership = MembershipFactory(user=self.user, organization=organization)
        membership.save()
        self.user.current_membership = membership
        self.user.save()
        response = self.client.post(url, data, format='json')
        self.access_token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        
    def logout(self):
        self.client.credentials(HTTP_AUTHORIZATION='')
