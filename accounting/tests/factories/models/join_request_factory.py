from faker import Faker
faker = Faker()
import factory

from accounting.models import JoinRequest


class JoinRequestFactory(factory.Factory):
    """
    JoinRequest factory
    """
    class Meta:
        model = JoinRequest
    id = factory.Sequence(lambda n: n)
    user = factory.SubFactory('accounting.tests.factories.models.user_factory.UserFactory')
    organization = factory.SubFactory('accounting.tests.factories.models.organization_factory.OrganizationFactory')
    #TODO: get existing membership id
    reviewed_by = 1
