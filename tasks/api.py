from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskSerializer
from .models import Tasks

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TaskSerializer
    
    @action(detail=True, methods=['post'])
    def done(self, request, pk=None):
        tasks =  self.get_object()
        tasks.done = not tasks.done
        tasks.save() 
        return Response({
            'status':'task done' if tasks.done else 'task undone'
            },status= status.HTTP_200_OK)