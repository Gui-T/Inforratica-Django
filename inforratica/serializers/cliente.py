from rest_framework.serializers import ModelSerializer

from inforratica.models import Cliente


class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = (
            "id",
            "nome",
            "cpf",
            "email",
            "endereco",
            "telefone",
        )
        depth = 1
