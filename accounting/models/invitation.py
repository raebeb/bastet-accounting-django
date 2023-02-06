from django.db import models


class Invitation(models.Model):
    uuid = models.UUIDField()
    email = models.EmailField()
    created_at = models.DateField(
        auto_now_add=True,
        editable=False,
    )
    updated_at = models.DateField(
        auto_now=True,
    )
    class Meta:
        verbose_name = "Invitation"
        verbose_name_plural = "Invitations"

    def __str__(self):
        pass
