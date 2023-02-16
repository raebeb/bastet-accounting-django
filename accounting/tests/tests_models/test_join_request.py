import unittest

from accounting.tests.factories.models.join_request_factory import JoinRequestFactory


class JoinRequestTestCase(unittest.TestCase):
    def setUp(self) -> None:
        """
        Set up test with join request instance
        :return:
        """
        self.join_request = JoinRequestFactory()
    def test_join_request_has_all_its_attributes(self):
        self.assertEqual(hasattr(self.join_request, 'user'), True)
        self.assertEqual(hasattr(self.join_request, 'organization'), True)
        self.assertEqual(hasattr(self.join_request, 'state'), True)
        self.assertEqual(hasattr(self.join_request, 'reviewed_by'), True)
        self.assertEqual(hasattr(self.join_request, 'created_at'), True)
        self.assertEqual(hasattr(self.join_request, 'updated_at'), True)

        self.assertEqual(f'{self.join_request.user.first_name} {self.join_request.user.last_name} - {self.join_request.organization.name}', self.join_request.__str__())


if __name__ == '__main__':
    unittest.main()
