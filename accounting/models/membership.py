from django.db import models
from django_fsm import FSMField, transition

from accounting.constants.states import MEMBERSHIP_STATES, CREATED, ACTIVE, INACTIVE, INVITED, REMOVED, SUSPENDED
from .user import User


class Membership(models.Model):
    """
    Membership model

    Relations:
        Belong to a user

    State machine:
        diagram: diagrams/states/membership.md
    """
    # Relations
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='memberships',
    )
    organization = models.ForeignKey(
        'Organization',
        on_delete=models.CASCADE,
        related_name='memberships',
    )

    # TODO: When the core is complete (part 1) this field will be required
    added_by = models.IntegerField(blank=True, null=True)
    # State machine
    state = FSMField(
        default=CREATED,
        choices=MEMBERSHIP_STATES,
        verbose_name='Membership state',
        protected=True)
    # Fields
    invitation_code = models.UUIDField(blank=True, null=True)
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Membership"
        verbose_name_plural = "Memberships"

    def __str__(self) -> str:
        return f'User: {self.user} - Added by {self.added_by}'

    @transition(field=state, source=CREATED, target=INVITED)
    def invite(self):
        """
        Method used to transition the membership to the invited state

        :param self: Refer to the object itself
        :return: A string

        """
        pass

    @transition(field=state, source=CREATED, target=ACTIVE)
    def create(self):
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