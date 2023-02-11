from django.db import models


class Company(models.Model):
    """
    Company model
    """
    name = models.CharField('name', max_length=50)
    #TODO: Change this name to something more meaningful
    tax_refered = models.CharField('tax refered', max_length=50)
    address = models.CharField('address', max_length=50)
    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self) -> str:
        return f'{self.name}'
