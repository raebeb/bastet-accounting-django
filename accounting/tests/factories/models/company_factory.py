from faker import Faker
faker = Faker()
import factory

from accounting.models import Company


class CompanyFactory(factory.Factory):
    """
    Company factory
    """
    class Meta:
        model = Company

    organization = factory.SubFactory('accounting.tests.factories.models.organization_factory.OrganizationFactory')
    name = factory.LazyAttribute(lambda o: faker.company())
    tax_refered = factory.LazyAttribute(lambda o: faker.company())
    password = factory.LazyAttribute(lambda o: faker.password())