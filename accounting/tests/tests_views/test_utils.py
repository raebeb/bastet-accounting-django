from accounting.models import User
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken
from accounting.tests.factories.models.organization_factory import OrganizationFactory
from accounting.tests.factories.models.user_factory import UserFactory
from accounting.tests.factories.models.membership_factory import MembershipFactory

class CustomAPITestCase(APITestCase):
    def setUp(self):
        self.organization = OrganizationFactory()
        self.user = UserFactory(username='fran')
        self.access_token = AccessToken.for_user(self.user)
        self.membership = MembershipFactory(user=self.user, organization=self.organization)
        self.user.current_membership = self.membership
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.access_token))

    def logout(self):
        self.client.logout()