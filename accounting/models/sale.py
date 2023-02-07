from django.db import models
from .transaction import Transaction

class Sale(Transaction):
    claim_date = models.DateField() # Fecha de reclamación
    total_iva_withheld = models.DecimalField(max_digits=20, decimal_places=2) # Total de IVA retenido
    partial_iva_withheld = models.DecimalField(max_digits=20, decimal_places=2) # IVA retenido parcial
    own_iva = models.DecimalField(max_digits=20, decimal_places=2) # IVA propio
    third_party_iva = models.DecimalField(max_digits=20, decimal_places=2) # IVA de terceros
    rut_liquid_commission_invoice = models.CharField(max_length=20) # RUT de la factura de comisión de liquidación
    net_liquid_commission_invoice = models.DecimalField(max_digits=20, decimal_places=2) # Comisión de liquidación neta
    commission_exempt_liquid_invoice = models.DecimalField(max_digits=20, decimal_places=2) # Comisión de liquidación exenta
    iva_out_of_time = models.DecimalField(max_digits=20, decimal_places=2) # IVA fuera de plazo
    type_of_document_reference = models.CharField(max_length=20) # Tipo de documento de referencia
    folio_reference_document = models.CharField(max_length=20) # Folio de documento de referencia
    foreign_recipients_identity_number = models.CharField(max_length=20) # Número de identidad de destinatarios extranjeros
    nationality_foreign_recipients = models.CharField(max_length=20) # Nacionalidad de destinatarios extranjeros
    construction_company_loan = models.DecimalField(max_digits=20, decimal_places=2) # Préstamo de empresa constructora
    free_zone_tax = models.DecimalField(max_digits=20, decimal_places=2) # Impuesto de zona franca
    packaging_warranty = models.DecimalField(max_digits=20, decimal_places=2) # Garantía de embalaje
    no_cost_sales_indicator = models.CharField(max_length=20) # Indicador de ventas sin costo
    periodic_service_indicator = models.CharField(max_length=20) # Indicador de servicio periódico
    non_billable_amount = models.DecimalField(max_digits=20, decimal_places=2) # Monto no facturable
    total_amount_period = models.DecimalField(max_digits=20, decimal_places=2) # Monto total del período
    ticket_sales_national_transportation = models.DecimalField(max_digits=20, decimal_places=2) # Ventas de boletos de transporte nacional
    sale_of_international_transportation_tickets = models.DecimalField(max_digits=20, decimal_places=2) # Venta de boletos de transporte internacional

    def __str__(self):
        return self.folio

    class Meta:
        verbose_name = 'Sale'
        verbose_name_plural = 'Sales'