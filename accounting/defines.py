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


DRAFT = 'draft'
CREATED = 'created'
PUBLISHED = 'published'
HIDDEN = 'hidden'
FINISHED = 'finished'
ACTIVE = 'active'
INACTIVE = 'inactive'
INVITED = 'invited'
REMOVED = 'removed'
SUSPENDED = 'suspended'
VERIFIED = 'verified'
BANNED = 'banned'
ACCEPTED = 'accepted'
REJECTED = 'rejected'


PLAN_STATES = (
  (DRAFT, DRAFT),
  (CREATED, CREATED),
  (PUBLISHED, PUBLISHED),
  (HIDDEN, HIDDEN),
  (FINISHED, FINISHED)
)

PLAN_ORGANIZATION_STATES = (
  (CREATED, CREATED),
  (ACTIVE, ACTIVE),
  (INACTIVE, INACTIVE)
)

MEMBERSHIP_STATES = (
  (CREATED, CREATED),
  (INVITED, INVITED),
  (ACTIVE, ACTIVE),
  (INACTIVE, INACTIVE),
  (REMOVED, REMOVED),
  (SUSPENDED, SUSPENDED)
)

USER_STATES = (
  (CREATED, CREATED),
  (VERIFIED, VERIFIED),
  (BANNED, BANNED)
)

JOIN_REQUEST_STATES = (
  (CREATED, CREATED),
  (ACCEPTED, ACCEPTED),
  (REJECTED, REJECTED)
)
  