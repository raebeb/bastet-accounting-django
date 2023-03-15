from faker import Faker

from accounting.models import Role

faker = Faker()

import factory


class RoleFactory(factory.Factory):
    class Meta:
        model = Role



    name = factory.LazyAttribute(lambda o: faker.name())
