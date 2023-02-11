from django.db import models

class Role(models.Model):
    """_summary_

    Relations:
        Has many Membership
    """
    # Fields
    name = models.CharField(max_length=255)
    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"

    def __str__(self) -> str:
        return f'{self.name}'
