import unittest

from accounting.tests.factories.models.role_factory import RoleFactory


class RoleTestCase(unittest.TestCase):
    def setUp(self) -> None:
        """
        Set up test with role instance
        :return: None
        """
        self.role = RoleFactory()

    def test_role_has_all_its_attributes(self) -> None:
        """
        Test role has all its attributes
        :return: None
        """
        self.assertEqual(hasattr(self.role, 'name'), True)


        self.assertEqual(self.role.name, self.role.__str__())


if __name__ == '__main__':
    unittest.main()
