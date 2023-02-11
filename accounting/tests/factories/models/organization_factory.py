import factory

from accounting.models import Organization


class OrganizationFactory(factory.Factory):
    class Meta:
        model = Organization

    name = factory.Sequence(lambda n: 'Organization {0}'.format(n))
    slug = factory.Sequence(lambda n: 'organization-{0}'.format(n))