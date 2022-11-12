from django.shortcuts import render
from rest_framework import viewsets
from to_do.models import ToDo
from to_do.serializers import ToDoSerializer
from rest_framework import permissions


class ToDoViewSet(viewsets.ModelViewSet):
    """
    This view set automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ToDo.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
