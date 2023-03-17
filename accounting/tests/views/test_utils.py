from accounting.models import User
from rest_framework.test import APITestCase
from accounting.tests.factories.models.organization_factory import OrganizationFactory
from accounting.tests.factories.models.user_factory import UserFactory
from accounting.tests.factories.models.membership_factory import MembershipFactory


class CustomAPITestCase(APITestCase):
    def setUp(self):
        self.organization = OrganizationFactory()
        self.user = UserFactory()
        self.membership = MembershipFactory(user=self.user, organization=self.organization)
        self.user.current_membership = self.membership
        self.client.login(username=self.user.username, password='password')

    def logout(self):
        self.client.logout()