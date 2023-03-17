import unittest
from accounting.tests.factories.models.membership_factory import MembershipFactory
from accounting.tests.factories.models.organization_factory import OrganizationFactory
from accounting.tests.factories.models.user_factory import UserFactory
from accounting.tests.factories.models.plan_factory import PlanFactory
from accounting.tests.factories.models.plan_organization_factory import PlanOrganizationFactory

class CustomTestCase(unittest.TestCase):
  def setUp(self):
    self.plan = PlanFactory()
    self.organization = OrganizationFactory()
    self.plan_organization = PlanOrganizationFactory(plan=self.plan, organization=self.organization)
    self.user = UserFactory()
    self.membership = MembershipFactory(user=self.user, organization=self.organization)

  def tearDown(self):
    pass