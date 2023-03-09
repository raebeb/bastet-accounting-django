import factory
from faker import Faker

from accounting.tests.factories.models.company_factory import CompanyFactory

faker = Faker()



from accounting.models import Accounting


class AccountingFactory(factory.Factory):
    """
    Organization factory
    """
    class Meta:
        model = Accounting

    id = factory.Sequence(lambda n: n)
    company = factory.SubFactory(CompanyFactory)
