from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from inforratica.models import Notebook
from inforratica.serializers import NotebookSerializer


class NotebookViewSet(ModelViewSet):
    queryset = Notebook.objects.all()
    serializer_class = NotebookSerializer
    permission_classes = [IsAuthenticated]