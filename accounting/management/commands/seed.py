from django.core.management.base import BaseCommand

from faker import Faker
faker = Faker()


from accounting.models import JoinRequest, Membership, Accounting, PlanOrganization, Company, Organization, Plan, \
    Role
from accounting.tests.factories import UserFactory, RoleFactory, PlanOrganizationFactory, PlanFactory, OrganizationFactory, MembershipFactory, JoinRequestFactory, AccountingFactory
from accounting.tests.factories.models.company_factory import CompanyFactory

# python manage.py seed --mode=refresh
"""clear all data and create new data"""
MODE_REFRESH = 'refresh'

# python manage.py seed --mode=clear
"""clear all data and do not create any object"""
MODE_CLEAR = 'clear'

class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def add_arguments(self, parser):
        parser.add_argument(
            '--mode',
            type=str,
            choices=[MODE_REFRESH, MODE_CLEAR],
            default=MODE_REFRESH,
            help='Seed mode',
        )

    def handle(self, *args, **options):
        mode = options['mode']
        if mode == MODE_REFRESH:
            self.stdout.write('Seeding the database with initial data...')
            self._seed()
            self.stdout.write('Seeding completed successfully.')
        elif mode == MODE_CLEAR:
            self.stdout.write('Clearing all data from the database...')
            self._clear()
            self.stdout.write('Clearing completed successfully.')


    #TODO: Implement the methods
    def _clear(self) -> None:
        """
        Execute method to clear the database
        :return: None
        """

        Role.objects.all().delete()
        Plan.objects.all().delete()
        Organization.objects.all().delete()
        Accounting.objects.all().delete()
        Company.objects.all().delete()
        PlanOrganization.objects.all().delete()
        Membership.objects.all().delete()
        JoinRequest.objects.all().delete()


    def _seed(self):
        """
        Execute method to seed th database
        :param mode: defines the behavior of the seed
        :return: None
        """
        if MODE_REFRESH:
            self.stdout.write('Clearing initial data...')
            self._clear()
            self.stdout.write('Clearing completed successfully.')

        for _ in range(10):
            user = create_user()
            role = create_role()
            plan = create_plan()
            organization = create_organization()
            company = create_company()
            plan_organization = create_plan_organization(organization=organization, plan=plan)
            accounting = create_accounting(company=company)
            membership = create_membership(user=user)
            join_request = create_join_request(organization=organization, user=user)

            try:
                user.save()
                print('User saved')
                role.save()
                print('Role saved')
                plan.save()
                print('Plan saved')
                organization.save()
                print('Organization saved')
                company.save()
                print('Company saved')
                plan_organization.save()
                print('PlanOrganization saved')
                accounting.save()
                print('Accounting saved')
                membership.save()
                print('Membership saved')
                join_request.save()
                print('JoinRequest saved')
            except Exception as e:
                print(f'Error -> {e}')
                return


# TODO: This method should be a abstract class
# example to use: create_object_factory_for('User', **kwargs)
def create_object_factory_for(object, **kwargs):
    """
    Create a new object.
    """
    factory_class = globals()[class_name + "Factory"]
    return factory_class(**kwargs)

def create_user():
    """
    Create a new User object.
    """
    user = UserFactory()
    return user


def create_role():
    """
    Create a new Role object.
    """
    role = RoleFactory()
    return role


def create_plan():
    """
    Create a new Plan object.
    """
    return PlanFactory()


def create_organization():
    """
    Create a new Organization object.
    """

    return OrganizationFactory()


def create_company():
    """
    Create a new Company object.
    """
    return CompanyFactory()


def create_plan_organization(organization, plan):
    """
    Create a new PlanOrganization object.
    """
    return PlanOrganizationFactory(organization=organization, plan=plan)


def create_accounting(company):
    """
    Create a new Accounting object.
    """
    return AccountingFactory(company=company)


def create_membership(user):
    """
    Create a new Membership object.
    """
    return MembershipFactory(user=user)


def create_join_request(organization, user):
    """
    Create a new JoinRequest object.
    """
    return JoinRequestFactory(organization=organization, user=user)