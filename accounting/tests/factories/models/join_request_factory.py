from faker import Faker

from accounting.tests.factories import OrganizationFactory, UserFactory

faker = Faker()
import factory

from accounting.models import JoinRequest


class JoinRequestFactory(factory.Factory):
    """
    JoinRequest factory
    """
    class Meta:
        model = JoinRequest
    user = factory.SubFactory(UserFactory)
    organization = factory.SubFactory(OrganizationFactory)
    #TODO: get existing membership id
    reviewed_by = 1
    created_at = faker.date_time()
