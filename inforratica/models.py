from django.db import models

class Computer(models.Model):
    cliente = models.CharField(max_length=100)
    placa_mae = models.CharField(max_length=100)
    processador = models.CharField(max_length=100)
    memoria = models.CharField(max_length=100)
    hd = models.CharField(max_length=100)
    ssd = models.CharField(max_length=100)
    fonte = models.CharField(max_length=100)
    gabinete = models.CharField(max_length=100)
    placa_video = models.CharField(max_length=100)
    preco = models.CharField(max_length=100)
    imagem = models.URLField(max_length=100)
    def __str__(self):
        return self.cliente