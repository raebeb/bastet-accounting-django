import unittest

from accounting.tests.factories.models.plan_factory import PlanFactory


class PlanTestCase(unittest.TestCase):
    def setUp(self) -> None:
        """
        Set up test with plan instance
        :return: None
        """
        self.plan = PlanFactory()
    def test_plan_has_all_its_attributes(self) -> None:
        """
        Test plan has all its attributes
        :return: None
        """
        self.assertEqual(hasattr(self.plan, 'name'), True)
        self.assertEqual(hasattr(self.plan, 'kind'), True)
        self.assertEqual(hasattr(self.plan, 'company_quantity'), True)
        self.assertEqual(hasattr(self.plan, 'created_at'), True)
        self.assertEqual(hasattr(self.plan, 'updated_at'), True)

        self.assertEqual(self.plan.name, self.plan.__str__())


if __name__ == '__main__':
    unittest.main()
