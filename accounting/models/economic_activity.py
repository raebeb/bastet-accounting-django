from django.db import models
from .company import Company

class EconomicActivity(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField()
    category = models.CharField(max_length=20)
    taxable = models.BooleanField()
    start_at = models.DateField()

    class Meta:
        verbose_name = 'Economic Activity'
        verbose_name_plural = 'Economic Activities'
    

# Obtener las actividades económicas de https://www.sii.cl/pagina/renta/suplemento2001/parte4/Listado_codigos.htm
