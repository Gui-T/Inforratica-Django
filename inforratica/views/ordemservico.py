from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from inforratica.models import OrdemServico
from usuario.models import Usuario
from inforratica.serializers import OrdemServicoSerializer, OrdemServicoReadSerializer

class OrdemServicoViewSet(ModelViewSet):
    queryset = OrdemServico.objects.all()
    serializer_class = OrdemServicoSerializer
    queryset = OrdemServico.objects.all().order_by("-data")
    permission_classes = [IsAuthenticated]

    # def get_serializer_class(self):
    #     if self.action == "list":
    #         return OrdemServicoReadSerializer
    #     return OrdemServicoSerializer

    @api_view(['GET'])
    def get_ordens_servico_cliente(request):
        # O usuário autenticado pode ser acessado via request.user
        cliente = request.user
        # Agora você pode recuperar as ordens de serviço associadas a esse cliente
        ordens_servico = OrdemServico.objects.filter(cliente=cliente)
        # Serializar e retornar as ordens de serviço como resposta
        serializer = OrdemServicoSerializer(ordens_servico, many=True)
        return Response(serializer.data)

    # def list(self, request):
    #     # breakpoint()
    #     queryset = OrdemServico.objects.filter(cliente__id=14)
    #     serializer = OrdemServicoReadSerializer(queryset, many=True)
    #     return Response(serializer.data)