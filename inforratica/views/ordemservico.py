from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from inforratica.models import OrdemServico, Cliente
from inforratica.serializers import OrdemServicoSerializer, OrdemServicoReadSerializer


class OrdemServicoViewSet(ModelViewSet):
    queryset = OrdemServico.objects.all()
    serializer_class = OrdemServicoSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return OrdemServicoReadSerializer
        return OrdemServicoSerializer