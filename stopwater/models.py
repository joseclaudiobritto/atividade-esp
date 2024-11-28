from django.db import models
from django.utils import choices

class Registro(models.Model):
    NIVEL = (
        ('N', 'Normal'),
        ('A', 'Alto')
    )
    data_registro = models.DateTimeField(auto_now_add=True)
    nivel = models.CharField(max_length = 1,choices=NIVEL, blank = False, null = False)

