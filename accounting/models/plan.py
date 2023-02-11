from django.db import models
from django_fsm import FSMField, transition

from accounting.constants.states import PLAN_STATES, DRAFT, CREATED, PUBLISHED, HIDDEN, FINISHED

class Plan(models.Model):
    """
    Plan model

    State machine:
        diagram: diagrams/state_machines/plan.md
    """
    # State machine
    state = FSMField(
      default=DRAFT,
      choices=PLAN_STATES,
      verbose_name='Plan state',
      protected=True)
    # Fields
    name = models.CharField(max_length=100)
    kind = models.CharField(max_length=50)
    company_quantities = models.IntegerField()

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Plan'
        verbose_name_plural = 'Plans'
    
    def __str__(self) -> str:
        return self.name
    
    @transition(field=state, source=DRAFT, target=CREATED)
    def create(self):
        pass

    @transition(field=state, source=CREATED, target=PUBLISHED)
    def publish(self):
        pass

    @transition(field=state, source=PUBLISHED, target=HIDDEN)
    def hide(self):
        pass

    @transition(field=state, source=HIDDEN, target=PUBLISHED)
    def show(self):
        pass
    
    @transition(field=state, source=HIDDEN, target=FINISHED)
    def finish(self):
        pass
