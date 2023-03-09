from django.core.management.base import BaseCommand

from accounting.models import User, JoinRequest, Membership, Accounting, PlanOrganization, Company, Organization, Plan, \
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
        self._clear()
        # if mode == MODE_CLEAR:
        #     return

        for _ in range(10):
            print(_)
            user = UserFactory()
            role = RoleFactory()
            plan = PlanFactory()
            plan.save()
            organization = OrganizationFactory()

            company = CompanyFactory()
            company.save()
            plan_organization = PlanOrganizationFactory(organization=organization, plan=plan)
            plan_organization.save()
            accounting = AccountingFactory(company=company)
            membership = MembershipFactory(user=user)
            print('*'*100)

            join_request = JoinRequestFactory(organization=organization, user=user)
            user.save()
            role.save()
            accounting.save()

            membership.save()
            join_request.save()


        #TODO: call here the methods to create the objects


