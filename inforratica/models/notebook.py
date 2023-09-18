from django.db import models


class Notebook(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    imagem = models.URLField(
        max_length=200,
        default="https://d2gg9evh47fn9z.cloudfront.net/1600px_COLOURBOX13277208.jpg",
    )

    def __str__(self):
        return f"{self.modelo}"