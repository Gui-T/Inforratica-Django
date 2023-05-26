from rest_framework.serializers import ModelSerializer

from inforratica.models import Computer

class ComputerSerializer(ModelSerializer):
    class Meta:
        model = Computer
        fields = "__all__"