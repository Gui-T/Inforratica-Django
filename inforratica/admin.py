from django.contrib import admin

from .models import Computador, Cliente, OrdemServico

admin.site.register(Computador)
admin.site.register(Cliente)
admin.site.register(OrdemServico)