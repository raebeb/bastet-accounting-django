import unittest

from accounting.tests.factories.models.membership_factory import MembershipFactory


class MembershipTestCase(unittest.TestCase):
    def setUp(self) -> None:
        """"
        Set up test with membership instance
        :return: None
        """
        self.membership = MembershipFactory()
    def test_membership_has_all_its_attributes(self):
        """
        Test membership has all its attributes
        :return: None
        """
        self.assertEqual(hasattr(self.membership, 'user'), True)
        self.assertEqual(hasattr(self.membership, 'organization'), True)
        self.assertEqual(hasattr(self.membership, 'roles'), True)
        self.assertEqual(hasattr(self.membership, 'added_by'), True)
        self.assertEqual(hasattr(self.membership, 'invitation_code'), True)
        self.assertEqual(hasattr(self.membership, 'created_at'), True)
        self.assertEqual(hasattr(self.membership, 'updated_at'), True)

        self.assertEqual(f'{self.membership.user.first_name} {self.membership.user.last_name} - {self.membership.organization.name}', self.membership.__str__())


if __name__ == '__main__':
    unittest.main()
