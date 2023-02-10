from django.db import models
from django_fsm import FSMField, transition

from accounting.constants.states import PLAN_ORGANIZATION_STATES, CREATED, ACTIVE, INACTIVE
from .organization import Organization
from .plan import Plan


class PlanOrganization(models.Model):
    # Relations
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    # State machine
    state = FSMField(
        default=CREATED,
        choices=PLAN_ORGANIZATION_STATES,
        verbose_name='PlanOrganization state',
        protected=True)
    # Fields
    start_date = models.DateField()
    end_date = models.DateField()
    contract_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'PlanOrganization'
        verbose_name_plural = 'PlanOrganizations'

    def __str__(self):
        return f'{self.plan.name} - {self.organization.name}'

    @transition(field=state, source=CREATED, target=ACTIVE)
    def activate(self):
        pass

    @transition(field=state, source=ACTIVE, target=INACTIVE)
    def deactivate(self):
        pass
    