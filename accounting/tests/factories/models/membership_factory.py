import factory
from faker import  Faker

faker = Faker()

from accounting.models import Membership

class MembershipFactory(factory.Factory):
    class Meta:
        model = Membership
    #TODO: add user and roles factories
    user = factory.SubFactory('accounting.tests.factories.models.user_factory.UserFactory')
    created_at = faker.date_time()
    updated_at = faker.date_time()

    #TODO: get existing membership id
    added_by = 1
    invitation_code = factory.LazyAttribute(lambda o: faker.uuid4())

