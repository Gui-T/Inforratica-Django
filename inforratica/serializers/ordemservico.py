from rest_framework.serializers import ModelSerializer, StringRelatedField

from inforratica.models import OrdemServico, Cliente, Computador


class ClienteDetalheOrdermServicoSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = ("id", "nome")

class ComputadorDetalheOrdermServicoSerializer(ModelSerializer):
    class Meta:
        model = Computador
        fields = ("id", "gabinete", "placa_mae", "processador", "memoria_ram", "hd", "ssd",  "fonte", "placa_de_video", "imagem")

class OrdemServicoReadSerializer(ModelSerializer):
    cliente = ClienteDetalheOrdermServicoSerializer()
    computador = ComputadorDetalheOrdermServicoSerializer()
    class Meta:
        model = OrdemServico
        fields = "__all__"

class OrdemServicoSerializer(ModelSerializer):
    class Meta:
        model = OrdemServico
        fields = "__all__"
