from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, StringRelatedField
from inforratica.models import OrdemServico, Computador, Notebook
from usuario.models import Usuario


class UsuarioDetalheOrdermServicoSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"
        depth = 2
        
class NotebookDetalheOrdermServicoSerializer(ModelSerializer):
    class Meta:
        model = Notebook
        fields = "__all__"
        depth = 2

class ComputadorDetalheOrdermServicoSerializer(ModelSerializer):
    class Meta:
        model = Computador
        fields = "__all__"
        depth = 2

class OrdemServicoReadSerializer(ModelSerializer):
    usuario = UsuarioDetalheOrdermServicoSerializer()
    computador = ComputadorDetalheOrdermServicoSerializer()
    notebook = NotebookDetalheOrdermServicoSerializer()

    class Meta:
        model = OrdemServico
        fields = "__all__"
        depth = 2
       
class OrdemServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdemServico
        fields = "__all__"