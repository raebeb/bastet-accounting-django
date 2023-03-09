import string

import factory
from faker import Faker

faker = Faker()

from accounting.models import Organization


class OrganizationFactory(factory.Factory):
    """
    Organization factory
    """
    class Meta:
        model = Organization

    id = factory.Sequence(lambda n: n)
    name = factory.Sequence(lambda n: 'Organization {0}'.format(n))
    slug = factory.Sequence(lambda n: 'organization-{0}'.format(n))
    join_code = ''.join(faker.random_elements(elements=(string.ascii_uppercase + string.digits), length=6))
    created_at = faker.date_time()
    updated_at = faker.date_time()

    @factory.post_generation
    def plans(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for plan in extracted:
                self.plans.add(plan)