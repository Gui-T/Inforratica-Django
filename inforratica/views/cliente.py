from rest_framework.viewsets import ModelViewSet

from inforratica.models import Cliente
from inforratica.serializers import ClienteSerializer

class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer