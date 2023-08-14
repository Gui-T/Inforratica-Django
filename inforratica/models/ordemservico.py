from django.db import models
from .computador import Computador
from .cliente import Cliente

class OrdemServico (models.Model):
    data = models.DateField(auto_now_add=True)
    descricao = models.TextField(max_length=500)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=None)

    computador = models.ForeignKey(Computador, on_delete=models.PROTECT, related_name="ordensservico", null=True, default=None)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name="ordensservico", null=True, default=None)
 
    def __str__(self):
        return f"{self.cliente} / {self.computador} / {self.data}"