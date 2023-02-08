from django.db import models
from .transaction import Transaction

class Purchase(Transaction):
    amount_of_recoverable_iva = models.DecimalField(max_digits=10, decimal_places=2) # Monto de IVA recuperable
    amount_of_non_recoverable_iva = models.DecimalField(max_digits=10, decimal_places=2) # Monto de IVA no recuperable
    non_recoverable_iva_code = models.CharField(max_length=2) # Código de IVA no recuperable
    net_fixed_asset = models.DecimalField(max_digits=10, decimal_places=2) # Monto neto de activo fijo
    fixed_asset_iva = models.DecimalField(max_digits=10, decimal_places=2) # Monto de IVA de activo fijo
    iva_common_use = models.DecimalField(max_digits=10, decimal_places=2) # Monto de IVA de uso común
    tax_without_right_to_credit = models.DecimalField(max_digits=10, decimal_places=2) # Monto de impuesto sin derecho a crédito
    iva_not_withheld = models.DecimalField(max_digits=10, decimal_places=2) # Monto de IVA no retenido
    cigars = models.DecimalField(max_digits=10, decimal_places=2) # Cigarrillos
    tobacco_cigarettes = models.DecimalField(max_digits=10, decimal_places=2) # Cigarrillos
    elaborated_cigars = models.DecimalField(max_digits=10, decimal_places=2) # Cigarrillos elaborado

    class Meta:
        verbose_name = 'Purchase'
        verbose_name_plural = 'Purchases'

    def __str__(self):
        # TODO: I dont know if must be number or folio
        return f'{self.number} - {self.document_type}'