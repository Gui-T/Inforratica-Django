from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Usuario
from .serializers import UsuarioSerializer
from usuario.models import Usuario  # Import the custom user model
from usuario.forms import CustomUserCreationForm  # Import the custom user creation form
from rest_framework.decorators import action  # Import action decorator
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed
from usuario.models import Usuario
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import Token
from rest_framework_simplejwt.exceptions import TokenError

def decode_jwt(token):
    try:
        token_obj = Token(token)
        payload = token_obj.payload
        return payload
    except TokenError as e:
        raise AuthenticationFailed('Token inválido')

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated] 

    def get(self, request):
        # Agora você pode acessar o usuário autenticado através de request.user
        user_id = request.user.id
        # Retorne informações do cliente associadas ao user_id
        user_info = get_cliente_info(user_id)
        return Response(user_info)



# class RegistrationViewSet(ModelViewSet):
#     @action(detail=False, methods=['post'])
#     def register(self, request):
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             # Your registration logic here
#             return Response({"message": "Registration successful"}, status=201)
#         return Response({"message": "Registration failed", "errors": form.errors}, status=400)

class CustomJWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
            return None

        try:
            decoded_payload = decode_jwt(token)
            user_id = decoded_payload.get('user_id')  # Suponha que seu payload contenha uma chave 'user_id'
            user = Usuario.objects.get(pk=user_id)  # Substitua 'Usuario' pelo nome do seu modelo de usuário personalizado
        except Usuario.DoesNotExist:
            raise AuthenticationFailed('Usuário não encontrado')
        except Exception as e:
            raise AuthenticationFailed('Token inválido')

        return (user, None)



