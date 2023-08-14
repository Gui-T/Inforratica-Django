from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from inforratica.models import OrdemServico, Cliente
from inforratica.serializers import OrdemServicoSerializer, OrdemServicoReadSerializer


class OrdemServicoViewSet(ModelViewSet):
    queryset = OrdemServico.objects.all()
    serializer_class = OrdemServicoSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return OrdemServicoReadSerializer
        return OrdemServicoSerializer