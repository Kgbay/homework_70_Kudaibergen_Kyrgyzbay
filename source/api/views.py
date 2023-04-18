from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from tracker.models import Task

from .serializers import TaskSerializer


class TaskView(APIView):
    def get(self, request, *args, **kwargs):
        objects = Task.objects.all()
        serializer = TaskSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DetailView(APIView):

    def get(self, request, pk=None):
        if pk:
            task = Task.objects.get(id=pk)
            serializer = TaskSerializer(task)
            return Response(serializer.data, status=status.HTTP_200_OK)
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateView(APIView):
    pass


class DeleteView(APIView):
    pass
