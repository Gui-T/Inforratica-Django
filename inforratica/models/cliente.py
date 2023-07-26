from django.db import models
from cpf_field.models import CPFField

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    cpf = CPFField(max_length=11)
    email = models.EmailField(max_length=254)
    telefone = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nome}"