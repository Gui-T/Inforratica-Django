from django.contrib import admin

from .models import Computador, Cliente, OrdemServico, Notebook

admin.site.register(Computador)
admin.site.register(Cliente)
admin.site.register(OrdemServico)
admin.site.register(Notebook)