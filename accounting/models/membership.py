from django.db import models
from .user import User
from .invitation import Invitation


class Membership(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='memberships',
    )
    invitation = models.ForeignKey(
        Invitation,
        on_delete=models.CASCADE,
        related_name='memberships',
    )
    added_by = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='added_memberships',
    )
    class Meta:
        verbose_name = "Membership"
        verbose_name_plural = "Memberships"

    def __str__(self):
        return f'User: {self.user} - Added by {self.added_by}'
