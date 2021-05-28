from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    author_id = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = Task
        fields = ['id', 'title', 'author', 'author_id',
                  'description', 'created', 'is_completed', ]
