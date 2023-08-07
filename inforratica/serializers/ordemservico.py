from rest_framework.serializers import ModelSerializer

from inforratica.models import OrdemServico

class OrdemServicoSerializer(ModelSerializer):
    class Meta:
        model = OrdemServico
        fields = "__all__"