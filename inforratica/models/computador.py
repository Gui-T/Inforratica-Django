from django.db import models

class Computador(models.Model):
    placa_mae = models.CharField(max_length=50)
    processador = models.CharField(max_length=50)
    memoria_ram = models.CharField(max_length=50)
    cooler = models.CharField(max_length=50, default="Stock")
    hd = models.CharField(max_length=50)
    ssd = models.CharField(max_length=50)
    fonte = models.CharField(max_length=50)
    gabinete = models.CharField(max_length=50)
    placa_de_video = models.CharField(max_length=50)
    imagem = models.URLField(max_length=200, default="https://d2gg9evh47fn9z.cloudfront.net/1600px_COLOURBOX13277208.jpg")
    def __str__(self):
        return f"{self.gabinete}"