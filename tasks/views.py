from rest_framework import viewsets

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.all()
        status_filter = self.request.query_params.get('status')

        if status_filter == 'completed':
            queryset = queryset.filter(status=True)
        elif status_filter == 'in_progress':
            queryset = queryset.filter(status=False)

        ordering = self.request.query_params.get('ordering', '-created_at')
        if ordering in ('created_at', '-created_at'):
            queryset = queryset.order_by(ordering)

        return queryset
