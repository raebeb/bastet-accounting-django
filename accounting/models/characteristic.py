from django.db import models

from .company import Company


# we have documented this because the name is very abstract
class Characteristic(models.Model):
    """
    Characteristic model
    """
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    start_at = models.DateField()

    class Meta:
        verbose_name = "Characteristic"
        verbose_name_plural = "Characteristics"

    def __str__(self) -> str:
        return self.name
