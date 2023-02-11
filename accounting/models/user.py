from django.contrib.auth.models import AbstractUser, Group, Permission
from django_fsm import FSMField, transition
from django.db import models

from accounting.constants.states import USER_STATES, CREATED, VERIFIED, BANNED

class User(AbstractUser):
    """
    
    Relations:
        Has many Group
        Has many Permission
        Has many Membership
        has many JoinRequest
    
    State machine:
        diagram: diagrams/state_machines/user.md
    """
    # Relations
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='accounting_user_permissions')
    # State machine
    state = FSMField(
        default=CREATED,
        choices=USER_STATES,
        verbose_name='User state',
        protected=True)

    # Fields
    current_sign_in_ip = models.GenericIPAddressField(null=True, blank=True)
    last_sign_in_ip = models.GenericIPAddressField(null=True, blank=True)
    current_organization = models.IntegerField()
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self) -> str:
        return f'{self.username}'

    @transition(field=state, source=CREATED, target=VERIFIED)
    def verify(self):
        pass

    @transition(field=state, source=[CREATED, VERIFIED], target=BANNED)
    def ban(self):
        pass
