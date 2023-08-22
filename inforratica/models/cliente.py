from django.db import models
from django.core.validators import MinLengthValidator


class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    email = models.EmailField(max_length=254)
    telefone = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    senha = models.CharField(
        max_length=30, validators=[MinLengthValidator(4)], default=""
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Clientes"
