from ..models import Accounting
import factory

class AccountingFactory(factory.Factory):
    class Meta:
        model = Accounting

    name = factory.Sequence(lambda n: 'Accounting {0}'.format(n))
    description = factory.Sequence(lambda n: 'Description {0}'.format(n))