from django.db import models
from .company import Company

class Accounting(models.Model):
    company = models.OneToOneField(Company, on_delete=models.RESTRICT)

    class Meta:
      verbose_name = "Accounting"
      verbose_name_plural = "Accountings"

    def __str__(self):
        pass
