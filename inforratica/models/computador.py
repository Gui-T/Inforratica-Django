from django.db import models
from uploader.models import Image 


class Computador(models.Model):
    placa_mae = models.CharField(max_length=50)
    processador = models.CharField(max_length=50)
    memoria_ram = models.CharField(max_length=80)
    cooler = models.CharField(max_length=50, default="Stock")
    hd = models.CharField(max_length=50)
    ssd = models.CharField(max_length=50)
    fonte = models.CharField(max_length=50)
    gabinete = models.CharField(max_length=50)
    placa_de_video = models.CharField(max_length=50)
    capa = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return f"{self.gabinete}"
