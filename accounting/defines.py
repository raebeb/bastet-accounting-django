DOCUMENT_TYPE_CHOICES = (
        # Electronic check
        ('', 'de_honorarios'),
        ('', 'de_compraventa'),
        ('', 'de_prestacion_de_servicios'),
        ('', 'comprobante_de_pago_electronico'),

        # libros_contables
        ('', 'libros_de_contabilidad_principal'),
        ('', 'libro_caja'),
        ('', 'libro_diario'),
        ('', 'libro_mayor'),
        ('', 'libro_de_honorarios'),
        ('', 'libro_de_inventarios_y_balances'),
        ('', 'libros_de_control'),
        ('', 'libro_fut'),
        ('', 'libros_auxiliares'),
        ('', 'libro_de_compras'),
        ('', 'libro_de_remuneraciones'),
        ('', 'libro_de_retenciones'),
        
        ('', 'notas_de_credito'),
        ('', 'notas_de_debito'),
        ('', 'letras_de_cambio'),
        ('', 'pagares'),
    )

TRANSACTION_TYPE_CHOICES = [
      ('', 'compra'),
      ('', 'venta')
    ]
