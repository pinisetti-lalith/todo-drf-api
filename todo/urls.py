from django.urls import path
from .views import TaskList, TaskDetail

app_name = 'todo'

urlpatterns = [
    path('tasks-list/', TaskList.as_view(), name='task-list'),
    path('tasks-detail/<int:pk>/', TaskDetail.as_view(), name='task-detail'),

]
