import factory
from faker import  Faker

from accounting.tests.factories.models.role_factory import RoleFactory

faker = Faker()

from accounting.models import Membership

class MembershipFactory(factory.Factory):
    class Meta:
        model = Membership
    #TODO: add user and roles factories
    user = factory.SubFactory('accounting.tests.factories.models.user_factory.UserFactory')
    id = factory.Sequence(lambda n: n)
    @factory.post_generation
    def roles(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for role in extracted:
                self.roles.add(role)

    #TODO: get existing membership id
    added_by = 1
    invitation_code = faker.uuid4()

