from django.db import models


class Company(models.Model):
    """
    Company model

    Relations:
        has one Membership
        has one Organization
    """
    name = models.CharField('name', max_length=50)
    tax_refered = models.CharField('tax refered', max_length=50) #rut
    # relations
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE, related_name='companies')
    chief_accountant = models.ForeignKey('Membership', on_delete=models.SET_NULL, related_name='companies', null=True, blank=True)
    #TODO: encrypt password
    password = models.CharField('password', max_length=200, null=True, blank=True)
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self) -> str:
        return f'{self.name}'
