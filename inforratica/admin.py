from django.contrib import admin

from .models import Computador, OrdemServico, Notebook

admin.site.register(Computador)
admin.site.register(OrdemServico)
admin.site.register(Notebook)