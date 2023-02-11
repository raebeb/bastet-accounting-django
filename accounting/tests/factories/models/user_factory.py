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

    current_sign_in_ip = faker.ipv4()
    last_sign_in_ip = faker.ipv4()
    current_organization = 1