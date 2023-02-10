from django.db import models
from django_fsm import FSMField, transition

from .user import User
from .organization import Organization
from ..defines import JOIN_REQUEST_STATES, CREATED, ACCEPTED, REJECTED


class JoinRequest(models.Model):
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
    
    def __str__(self):
        return f'User: {self.user} - Organization: {self.organization}'
    
    @transition(field=state, source=CREATED, target=ACCEPTED)
    def accept(self):
        pass
    
    @transition(field=state, source=CREATED, target=REJECTED)
    def reject(self):
        pass