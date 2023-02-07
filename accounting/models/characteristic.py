from django.db import models
from .company import Company

# we have documented this because the name is very abstract 
class Characteristic(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    start_at = models.DateField()

    class Meta:
      verbose_name = "Characteristic"
      verbose_name_plural = "Characteristics"

