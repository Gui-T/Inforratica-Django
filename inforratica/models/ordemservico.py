from django.core.exceptions import ValidationError
from django.db import models
from .computador import Computador
from usuario.models import Usuario
from .notebook import Notebook

class OrdemServico(models.Model):
    data = models.DateField(auto_now_add=True)
    descricao = models.TextField(max_length=500)
    valor = models.DecimalField( max_digits=10, decimal_places=2, null=True, default=None)
    status = models.TextField(max_length=50, null=True, default=None)
    computador = models.ForeignKey(
        Computador,
        on_delete=models.PROTECT,
        related_name="ordensservico",
        null=True,
        default=None,
    )
    notebook = models.ForeignKey(
        Notebook,
        on_delete=models.PROTECT,
        related_name="ordensservico",
        null=True,
        default=None,
    )
    usuario = models.ForeignKey(
        Usuario,    
        on_delete=models.CASCADE,
        related_name="ordensservico",
        default=None,
        null=True,
    )
