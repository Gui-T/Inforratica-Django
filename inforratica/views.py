from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from inforratica.models import Computer
from inforratica.serializers import ComputerSerializer

class ComputerViewSet(ModelViewSet):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer