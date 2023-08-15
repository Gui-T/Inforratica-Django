from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from inforratica.models import Cliente
from inforratica.serializers import ClienteSerializer


class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    # permission_classes = [IsAuthenticated]
