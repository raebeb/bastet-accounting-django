from django.db import models

from .company import Company


class Accounting(models.Model):
    """
    Accounting model
    """
    company = models.OneToOneField(Company, on_delete=models.RESTRICT)

    class Meta:
        verbose_name = "Accounting"
        verbose_name_plural = "Accountings"

    def __str__(self) -> str:
        return f'Accountign for {self.company.name}'
