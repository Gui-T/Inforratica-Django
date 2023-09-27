from django.db import models
from uploader.models import Image 


class Notebook(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    capa = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return f"{self.modelo}"