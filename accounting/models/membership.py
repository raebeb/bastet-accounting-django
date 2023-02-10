from django.db import models
from django_fsm import FSMField, transition

from .user import User
from accounting.constants.states import MEMBERSHIP_STATES, CREATED, ACTIVE, INACTIVE, INVITED, REMOVED, SUSPENDED


class Membership(models.Model):
    # Relations
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='memberships',
    )
    added_by = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='added_memberships',
    )
    # TODO: i need to add a relation to the role model, must be many to many

    # State machine
    state = FSMField(
      default=CREATED,
      choices=MEMBERSHIP_STATES,
      verbose_name='Membership state',
      protected=True)

    # Fields
    invitation_code = models.UUIDField()
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Membership"
        verbose_name_plural = "Memberships"

    def __str__(self):
        return f'User: {self.user} - Added by {self.added_by}'

    @transition(field=state, source=CREATED, target=INVITED)
    def invite(self):
        pass

    @transition(field=state, source=INVITED, target=ACTIVE)
    def activate(self):
        pass

    @transition(field=state, source=ACTIVE, target=INACTIVE)
    def deactivate(self):
        pass

    @transition(field=state, source=ACTIVE, target=REMOVED)
    def remove(self):
        pass

    @transition(field=state, source=ACTIVE, target=SUSPENDED)
    def suspend(self):
        pass