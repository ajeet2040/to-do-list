from django.shortcuts import render
from rest_framework import viewsets
from to_do.models import ToDo
from to_do.serializers import ToDoSerializer
from rest_framework import permissions
from to_do.permissions import IsOwnerOrReadOnly


# Create your views here.
class ToDoViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    # def perform_create(self, serializer):
    #     pass
