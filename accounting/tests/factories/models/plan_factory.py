import factory
from faker import Faker

from accounting.models import Plan

faker = Faker()

class PlanFactory(factory.Factory):
    class Meta:
        model = Plan

    id = factory.Sequence(lambda n: n)
    name = factory.Sequence(lambda n: 'Plan {0}'.format(n))
    kind = factory.Sequence(lambda n: 'kind-{0}'.format(n))
    company_quantity = factory.LazyAttribute(lambda o: faker.random_int(min=1, max=10))
    created_at = faker.date_time()
    updated_at = faker.date_time()

