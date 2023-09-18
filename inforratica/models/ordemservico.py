from django.core.exceptions import ValidationError
from django.db import models
from .computador import Computador
from .cliente import Cliente
from .notebook import Notebook

class OrdemServico(models.Model):
    data = models.DateField(auto_now_add=True)
    descricao = models.TextField(max_length=500)
    valor = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, default=None
    )
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
    cliente = models.ForeignKey(
        Cliente,    
        on_delete=models.PROTECT,
        related_name="ordensservico",
        default=None,
    )
    
    def clean(self):
        # Use Q objects to check if either 'computador' or 'notebook' is selected
        if not (self.computador or self.notebook):
            raise ValidationError(
                'Please select either a computador or a notebook.')
        if self.computador and self.notebook:
            raise ValidationError(
                'Please select either a computador or a notebook, not both.')
