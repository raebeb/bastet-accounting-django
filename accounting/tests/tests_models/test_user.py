import unittest

from ..factories.models.user_factory import UserFactory


class UserTestCase(unittest.TestCase):
    def setUp(self) -> None:
        """
        Set up test with user instance
        :return: None
        """
        self.user = UserFactory()
    def test_user_has_all_its_attributes(self) -> None:
        """
        Test user has all its attributes
        :return: None
        """
        self.assertEqual(hasattr(self.user, 'groups'), True)
        self.assertEqual(hasattr(self.user, 'user_permissions'), True)
        self.assertEqual(hasattr(self.user, 'state'), True)
        self.assertEqual(hasattr(self.user, 'current_sign_in_ip'), True)
        self.assertEqual(hasattr(self.user, 'last_sign_in_ip'), True)
        self.assertEqual(hasattr(self.user, 'current_membership'), True)
        self.assertEqual(hasattr(self.user, 'created_at'), True)
        self.assertEqual(hasattr(self.user, 'updated_at'), True)

        self.assertEqual(self.user.username, self.user.__str__())


if __name__ == '__main__':
    unittest.main()
