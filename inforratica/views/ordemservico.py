from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import status

from inforratica.models import OrdemServico
from usuario.models import Usuario
from inforratica.serializers import OrdemServicoSerializer, OrdemServicoReadSerializer


class OrdemServicoViewSet(ModelViewSet):
    queryset = OrdemServico.objects.all()
    serializer_class = OrdemServicoSerializer
    queryset = OrdemServico.objects.all().order_by("-data")
    depth = 2
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['GET'])
    def user_orders(self, request):
        user = request.user

        if user.id == 1:
            user_orders = OrdemServico.objects.all()
        else:
            user_orders = OrdemServico.objects.filter(usuario=user.id)

        serializer = OrdemServicoReadSerializer(user_orders, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
