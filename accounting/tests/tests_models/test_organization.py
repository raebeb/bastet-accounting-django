from .test_utils import CustomTestCase

from accounting.tests.factories.models.organization_factory import OrganizationFactory
from accounting.tests.factories.models.plan_factory import PlanFactory


class OrganizationTestCase(CustomTestCase):
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

        self.assertEqual(self.organization.__str__(), self.organization.name)


if __name__ == '__main__':
    unittest.main()
