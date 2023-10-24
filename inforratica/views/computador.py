from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from inforratica.models import Computador
from inforratica.serializers import ComputadorSerializer


class ComputadorViewSet(ModelViewSet):
    queryset = Computador.objects.all()
    serializer_class = ComputadorSerializer
    permission_classes = [IsAuthenticated]
