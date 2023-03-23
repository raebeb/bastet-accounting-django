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

    name = factory.Sequence(lambda n: 'Organization {0}'.format(n))
    slug = factory.LazyAttribute(lambda o: ''.join(faker.random_letters(length=10)).replace(' ', ''))
    join_code = factory.LazyAttribute(lambda o: ''.join(faker.random_letters(length=6)).replace(' ', ''))
