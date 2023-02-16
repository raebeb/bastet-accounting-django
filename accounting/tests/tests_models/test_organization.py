import unittest

from accounting.tests.factories.models.organization_factory import OrganizationFactory
from accounting.tests.factories.models.plan_factory import PlanFactory


class OrganizationTestCase(unittest.TestCase):
    def setUp(self) -> None:
        """
        Set up test with organization instance
        :return: None
        """
        self.plan = PlanFactory()
        self.organization = OrganizationFactory()
    def test_organization_has_all_its_attributes(self) -> None:
        """
        Test organization has all its attributes
        :arg: self
        :return: None
        """
        self.assertEqual(hasattr(self.organization, 'plans'), True)
        self.assertEqual(hasattr(self.organization, 'name'), True)
        self.assertEqual(hasattr(self.organization, 'slug'), True)
        self.assertEqual(hasattr(self.organization, 'join_code'), True)
        self.assertEqual(hasattr(self.organization, 'created_at'), True)
        self.assertEqual(hasattr(self.organization, 'updated_at'), True)

        self.assertEqual(self.organization.__str__(), self.organization.name


if __name__ == '__main__':
    unittest.main()
