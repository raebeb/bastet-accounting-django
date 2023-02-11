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
    slug = factory.Sequence(lambda n: 'organization-{0}'.format(n))
    join_code = faker.pystr_format(string_format='??????{{random_int}}{{random_letter}}', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ')