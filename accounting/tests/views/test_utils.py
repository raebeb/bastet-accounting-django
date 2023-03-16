from accounting.models import User
from rest_framework.test import APITestCase
from accounting.models import Organization, Membership

class CustomAPITestCase(APITestCase):
    def setUp(self):
        self.organization = Organization.objects.create(name='organization', slug='123', join_code='test')
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.membership = Membership.objects.create(user=self.user, organization=self.organization)
        self.user.current_membership = self.membership
        self.user.save()
        self.client.login(username='testuser', password='testpassword')

    def Logout(self):
        self.client.logout()