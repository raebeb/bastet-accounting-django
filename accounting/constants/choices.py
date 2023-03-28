DOCUMENT_TYPE_CHOICES = (
    # Electronic check
    ('DH', 'de_honorarios'),
    ('DCV', 'de_compraventa'),
    ('DPDS', 'de_prestacion_de_servicios'),
    ('CDPE', 'comprobante_de_pago_electronico'),

    # libros_contables
    ('LDCP', 'libros_de_contabilidad_principal'),
    ('LC', 'libro_caja'),
    ('LD', 'libro_diario'),
    ('LM', 'libro_mayor'),
    ('LDH', 'libro_de_honorarios'),
    ('LDIYB', 'libro_de_inventarios_y_balances'),
    ('LDC', 'libros_de_control'),
    ('LF', 'libro_fut'),
    ('LA', 'libros_auxiliares'),
    ('LDCOMP', 'libro_de_compras'),
    ('LDREM', 'libro_de_remuneraciones'),
    ('LDRET', 'libro_de_retenciones'),

    ('NDC', 'notas_de_credito'),
    ('NDB', 'notas_de_debito'),
    ('LETDCAM', 'letras_de_cambio'),
    ('P', 'pagares'),
)

TRANSACTION_TYPE_CHOICES = [
    ('C', 'compra'),
    ('V', 'venta')
]
