from django.http import JsonResponse
from django.views import View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from tracker.models import Task

from .serializers import TaskSerializer


class TaskSimpleView(View):
    def get(self, request, *args, **kwargs):
        objects = Task.objects.all()
        serializer = TaskSerializer(objects, many=True)
        return JsonResponse(serializer.data)

class TaskView(APIView):
    def get(self, request, *args, **kwargs):
        objects = Task.objects.all()
        serializer = TaskSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
