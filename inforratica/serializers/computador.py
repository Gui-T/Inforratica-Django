from rest_framework.serializers import ModelSerializer

from inforratica.models import Computador


class ComputadorSerializer(ModelSerializer):
    class Meta:
        model = Computador
        fields = "__all__"
