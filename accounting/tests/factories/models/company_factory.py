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
    name = faker.company()
    tax_refered = faker.name()
    address = faker.address()
