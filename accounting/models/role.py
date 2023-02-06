from django.db import models

from accounting.models.membership import Membership


class Role(models.Model):
    membership = models.ForeignKey(
        Membership,
        on_delete=models.CASCADE,
        related_name='roles',
    )
    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"

    def __str__(self):
        return f'{self.membership} - {self.name}'
