import factory
from faker import Faker
faker = Faker()

from accounting.models import User


class UserFactory(factory.Factory):
    """
    User factory
    """
    class Meta:
        model = User


    username = factory.Sequence(lambda n: 'user{0}'.format(n))
    current_sign_in_ip = factory.LazyAttribute(lambda o: faker.ipv4())
    last_sign_in_ip = factory.LazyAttribute(lambda o: faker.ipv4())
    current_organization = 1
    created_at = faker.date_time()
    updated_at = faker.date_time()
    @factory.post_generation
    def groups(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for group in extracted:
                self.groups.add(group)

    @factory.post_generation
    def user_permissions(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for permission in extracted:
                self.user_permissions.add(permission)
