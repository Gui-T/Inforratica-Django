from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, StringRelatedField
from inforratica.models import OrdemServico, Computador
from usuario.models import Usuario


class UsuarioDetalheOrdermServicoSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"


class ComputadorDetalheOrdermServicoSerializer(ModelSerializer):
    class Meta:
        model = Computador
        fields = (
            "id",
            "gabinete",
            "placa_mae",
            "processador",
            "memoria_ram",
            "hd",
            "ssd",
            "fonte",
            "placa_de_video",
        )


class OrdemServicoReadSerializer(ModelSerializer):
    usuario = UsuarioDetalheOrdermServicoSerializer()
    computador = ComputadorDetalheOrdermServicoSerializer()

    class Meta:
        model = OrdemServico
        fields = "__all__"


class OrdemServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdemServico
        fields = "__all__"

    def validate(self, data):
        computador = data.get("computador")
        notebook = data.get("notebook")

        if computador is None and notebook is None:
            raise serializers.ValidationError(
                "Please select either a computador or a notebook."
            )

        if computador and notebook:
            raise serializers.ValidationError(
                "Please select either a computador or a notebook, not both."
            )

        return data