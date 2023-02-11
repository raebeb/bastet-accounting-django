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
    is_active = True
    start_date = faker.date()
    end_date = start_date + timedelta(days=30)
    price = faker.pydecimal(left_digits=2, right_digits=2, positive=True)