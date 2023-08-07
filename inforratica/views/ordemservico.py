from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from inforratica.models import OrdemServico
from inforratica.serializers import OrdemServicoSerializer

class OrdemServicoViewSet(ModelViewSet):
    queryset = OrdemServico.objects.all()
    serializer_class = OrdemServicoSerializer