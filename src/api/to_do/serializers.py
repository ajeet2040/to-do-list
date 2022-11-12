from rest_framework import serializers
from to_do.models import ToDo


class ToDoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ToDo
        fields = ['id', 'created_at', 'title', 'description', 'is_completed']
