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

    id = factory.Sequence(lambda n: n)
    name = factory.LazyAttribute(lambda o: faker.company())
    tax_refered = factory.LazyAttribute(lambda o: faker.company())
    address = factory.LazyAttribute(lambda o: faker.address())
