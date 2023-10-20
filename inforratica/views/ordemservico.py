from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import status
from django.contrib.auth.models import Group
from django.http import Http404

from inforratica.models import OrdemServico
from usuario.models import Usuario
from inforratica.serializers import OrdemServicoSerializer, OrdemServicoReadSerializer


class OrdemServicoViewSet(ModelViewSet):
    queryset = OrdemServico.objects.all()
    serializer_class = OrdemServicoSerializer
    queryset = OrdemServico.objects.all().order_by("-data")
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['GET'])
    def user_orders(self, request):
        # Recupere o usuário autenticado
        user = request.user

        # Verifique se o ID do usuário autenticado é igual a 1 (ou outro valor específico)
        if user.id == 1:
            # Se o ID for igual a 1, recupere todas as ordens de serviço
            user_orders = OrdemServico.objects.all()
        else:
            # Caso contrário, recupere as ordens de serviço associadas ao ID do usuário
            user_orders = OrdemServico.objects.filter(usuario=user.id)

        # Serialize as ordens de serviço
        serializer = OrdemServicoReadSerializer(user_orders, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
