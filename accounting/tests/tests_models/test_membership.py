from .test_utils import CustomTestCase

class MembershipTestCase(CustomTestCase):
    def test_membership_has_all_its_attributes(self):
        """
        Test membership has all its attributes
        :return: None
        """
        self.assertEqual(hasattr(self.membership, 'user'), True)
        self.assertEqual(hasattr(self.membership, 'added_by'), True)
        self.assertEqual(hasattr(self.membership, 'invitation_code'), True)
        self.assertEqual(hasattr(self.membership, 'created_at'), True)
        self.assertEqual(hasattr(self.membership, 'updated_at'), True)

        self.assertEqual( f'User: {self.membership.user} - Added by {self.membership.added_by}', self.membership.__str__())


if __name__ == '__main__':
    unittest.main()
