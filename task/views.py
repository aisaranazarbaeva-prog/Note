from django.core.serializers import serialize
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions,status
from .models import Task
from .serializer import TaskSerializer

class ListTask(APIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get(self,request,*args, **kwargs):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self,request, *args, **kwargs):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Detail(APIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    def get(self,request,task_id,*args, **kwargs):
        task = get_object_or_404(Task,pk=task_id)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, task_id, *args, **kwargs):
        task = get_object_or_404(Task, pk=task_id)
        serializer = TaskSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, task_id, *args, **kwargs):
        task = get_object_or_404(Task, pk=task_id)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)