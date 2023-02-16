from django.db import models

from .company import Company


class EconomicActivity(models.Model):
    """
    Economic Activity model
    """
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField()
    category = models.CharField(max_length=20)
    taxable = models.BooleanField()
    start_at = models.DateField()

    class Meta:
        verbose_name = 'Economic Activity'
        verbose_name_plural = 'Economic Activities'

    def __str__(self) -> str:
        return f'{self.code} - {self.name}'
