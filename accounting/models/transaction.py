from django.db import models
from .accounting import Accounting
from ..defines import DOCUMENT_TYPE_CHOICES, TRANSACTION_TYPE_CHOICES

class Transaction(models.Model):
    accounting = models.ForeignKey(Accounting, on_delete=models.CASCADE)

    number = models.IntegerField()
    document_type = models.CharField(max_length=20, choices=DOCUMENT_TYPE_CHOICES)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPE_CHOICES)
    # Rut del cliente o proveedor
    rut_customer_or_supplier = models.CharField(max_length=20)
    company_name = models.CharField(max_length=100)
    folio = models.CharField(max_length=20)
    document_date = models.DateField()
    # Fecha de acuso de recibo
    acknowledgement_date = models.DateField()
    exempt_amount = models.DecimalField(max_digits=10 ,decimal_places= 3)
    net_total = models.DecimalField(max_digits=10 ,decimal_places= 3)
    total_amount = models.DecimalField(max_digits=10 ,decimal_places= 3)
    code_other_tax = models.CharField(max_length=20)
    value_other_tax = models.DecimalField(max_digits=10 ,decimal_places= 3)
    other_tax = models.CharField(max_length=20)
    nce_or_nde_on_purchase_invoice = models.CharField(max_length=20)

    class Meta:
        abstract = True
