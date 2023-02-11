import factory
from faker import  Faker
faker = Faker()

from accounting.models import Membership

class MembershipFactory(factory.Factory):
    class Meta:
        model = Membership
    #TODO: add user and roles factories
    user = factory.SubFactory('accounting.tests.factories.models.user_factory.UserFactory')
    organization = factory.SubFactory('accounting.tests.factories.models.organization_factory.OrganizationFactory')
    plan = factory.SubFactory('accounting.tests.factories.models.plan_factory.PlanFactory')
    roles = factory.SubFactory('accounting.tests.factories.models.role_factory.RoleFactory')

    #TODO: get existing membership id
    added_by = 1
    invitation_code = faker.uuid4()

