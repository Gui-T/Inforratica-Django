from rest_framework.viewsets import ModelViewSet
# from rest_framework.response import Response

from .models import Usuario
from .serializers import UsuarioSerializer
# from usuario.models import Usuario  # Import the custom user model
# from usuario.forms import CustomUserCreationForm  # Import the custom user creation form
# from rest_framework.decorators import action  # Import action decorator

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
