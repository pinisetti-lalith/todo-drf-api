from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Task
from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly
from .serializers import TaskSerializer
from rest_framework.exceptions import ValidationError

# Create your views here.


class TaskList(ListCreateAPIView):
    # queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(author=user)


class TaskDetail(RetrieveUpdateDestroyAPIView):
    # queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(author=user)

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)
