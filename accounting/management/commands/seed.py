from django.core.management.base import BaseCommand

from faker import Faker
faker = Faker()

from accounting.tests.factories import UserFactory, RoleFactory, PlanOrganizationFactory, PlanFactory, OrganizationFactory, MembershipFactory, JoinRequestFactory, AccountingFactory, CompanyFactory

from accounting.models import JoinRequest, Membership, Accounting, PlanOrganization, Company, Organization, Plan, \
    Role, User

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

        # User.objects.all().delete()
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
            user = create_object_factory_for('User')
            role = create_object_factory_for('Role')
            plan = create_object_factory_for('Plan')
            organization = create_object_factory_for('Organization')
            company = create_object_factory_for('Company')
            plan_organization = create_object_factory_for('PlanOrganization', plan=plan, organization=organization)
            accounting = create_object_factory_for('Accounting', company=company)
            membership = create_object_factory_for('Membership', user=user)
            join_request = create_object_factory_for('JoinRequest', organization=organization, user=user)

            try:
                user.save()
                role.save()
                plan.save()
                organization.save()
                company.save()
                plan_organization.save()
                accounting.save()
                membership.save()
                join_request.save()

            except Exception as e:
                print(f'Error -> {e}')
                return


def create_object_factory_for(model_name: str, **kwargs) -> object:
    """
    Create a new object.
    """
    factory_class = globals()[model_name + "Factory"]
    return factory_class(**kwargs)


