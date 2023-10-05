from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Usuario
from .serializers import UsuarioSerializer
from usuario.models import Usuario  # Import the custom user model
from usuario.forms import CustomUserCreationForm  # Import the custom user creation form
from rest_framework.decorators import action  # Import action decorator

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    
class RegistrationViewSet(ModelViewSet):
    @action(detail=False, methods=['post'])
    def register(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Your registration logic here
            return Response({"message": "Registration successful"}, status=201)
        return Response({"message": "Registration failed", "errors": form.errors}, status=400)
