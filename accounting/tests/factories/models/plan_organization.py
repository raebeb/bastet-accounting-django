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

    id = factory.Sequence(lambda n: n)
    plan = factory.SubFactory(PlanFactory)
    organization = factory.SubFactory(OrganizationFactory)
    state = 'CREATED'
    start_date = faker.date_object()
    end_date = start_date + timedelta(days=30)
    created_at = faker.date_time()
    updated_at = faker.date_time()
    price = faker.pydecimal(left_digits=2, right_digits=2, positive=True)