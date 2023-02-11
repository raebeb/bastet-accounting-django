from django.db import models

from .company import Company


class Stakeholder(models.Model):
    """

    Relations:
        Belong to a company
    """
    # Relations
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    # Fields
    name = models.CharField(max_length=100)
    rut = models.CharField(max_length=20)
    current_partner = models.BooleanField(default=False)
    legal_representative = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Stakeholder'
        verbose_name_plural = 'Stakeholders'

    def __str__(self) -> str:
        return f'{self.name} - representative?: {self.legal_representative} - partner?: {self.current_partnership}'
