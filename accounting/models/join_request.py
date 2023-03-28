from django.db import models
from django_fsm import FSMField, transition

from accounting.constants.states import JOIN_REQUEST_STATES, CREATED, ACCEPTED, REJECTED
from .organization import Organization
from .user import User

class JoinRequest(models.Model):
    """
    Join request model

    Relations:
        Belong to a user
        Belong to an organization
    
    State machine:
        diagram: diagrams/states/join_request.md
    """
    # Relations
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='join_requests',
    )
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='join_requests',
    )
    # State machine
    state = FSMField(
        default=CREATED,
        choices=JOIN_REQUEST_STATES,
        verbose_name='Join request state',
        protected=True)
    # Fields
    reviewed_by = models.IntegerField()
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Join request"
        verbose_name_plural = "Join requests"

    def __str__(self) -> str:
        return f'User: {self.user} - Organization: {self.organization}'

    @transition(field=state, source=CREATED, target=ACCEPTED)
    def accept(self) -> None:
        """
        Method used to transition the join request to the accepted state
        :arg self: The join request instance
        :return: None
        """
        pass

    @transition(field=state, source=CREATED, target=REJECTED)
    def reject(self) -> None:
        """
        Method used to transition the join request to the rejected state
        arg self: The join request instance
        return: None
        """
        pass
