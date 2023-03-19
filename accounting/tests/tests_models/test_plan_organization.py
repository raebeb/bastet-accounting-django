import unittest

from accounting.tests.factories.models.organization_factory import OrganizationFactory
from accounting.tests.factories.models.plan_factory import PlanFactory
from accounting.tests.factories.models.plan_organization_factory import PlanOrganizationFactory


class PlanOrganizationTestCase(unittest.TestCase):
    def setUp(self) -> None:
        """
        Set up test with plan instance
        :return: None
        """
        self.plan = PlanFactory()
        self.organization = OrganizationFactory()
        self.plan_organization = PlanOrganizationFactory(plan=self.plan, organization=self.organization)
    @unittest.skip('Not implemented yet')
    def test_plan_organization_has_all_its_attributes(self) -> None:
        """
        Test plan organization has all its attributes
        :return: None
        """
        self.assertEqual(hasattr(self.plan_organization, 'plan'), True)
        self.assertEqual(hasattr(self.plan_organization, 'organization'), True)
        self.assertEqual(hasattr(self.plan_organization, 'state'), True)
        self.assertEqual(hasattr(self.plan_organization, 'start_date'), True)
        self.assertEqual(hasattr(self.plan_organization, 'end_date'), True)
        self.assertEqual(hasattr(self.plan_organization, 'price'), True)
        self.assertEqual(hasattr(self.plan_organization, 'created_at'), True)
        self.assertEqual(hasattr(self.plan_organization, 'updated_at'), True)


        self.assertEqual(f'{self.plan.name} - {self.organization.name}', self.plan_organization.__str__())


if __name__ == '__main__':
    unittest.main()
