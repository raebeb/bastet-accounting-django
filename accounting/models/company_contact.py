from django.db import models

from .company import Company


class CompanyContact(models.Model):
    """
    Company Contact model
    """
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    cellphone_number = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Company Contact"
        verbose_name_plural = "Company Contacts"

    def __str__(self) -> str:
        return f"Contact fot {self.company.name}: {self.name} - {self.phone_number}"
