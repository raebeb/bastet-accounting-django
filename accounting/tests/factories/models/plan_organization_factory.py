from datetime import timedelta

import factory
from faker import Faker

from accounting.models import PlanOrganization
from .organization_factory import OrganizationFactory
from .plan_factory import PlanFactory

faker = Faker()


class PlanOrganizationFactory(factory.Factory):
    class Meta:
        model = PlanOrganization

    plan = factory.SubFactory(PlanFactory)
    organization = factory.SubFactory(OrganizationFactory)
    start_date = faker.date_time()
    end_date = faker.date_time() + timedelta(days=30)
    price = factory.LazyAttribute(lambda o: faker.random_int(min=1, max=10))

