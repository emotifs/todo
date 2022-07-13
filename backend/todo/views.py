from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.routers import Response

from .models import Task
from .serializers import TaskSerializer


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'Task List': reverse(task_list, request=request),
        'Task Create': reverse(task_create, request=request),
    }
    return Response(api_urls)


@api_view(['GET'])
def task_list(request):
    tasks = Task.objects.all().order_by('created')
    serializer = TaskSerializer(tasks, many=True)
    for i in serializer.data:
        i['LINK'] = reverse(task, kwargs={'id': i['id']}, request=request)
        i['UPDATE'] = reverse(task_edit, kwargs={'id': i['id']}, request=request)
        i['DELETE'] = reverse(task_delete, kwargs={'id': i['id']}, request=request)
    return Response(serializer.data)


@api_view(['GET'])
def task(request, id):
    tasks = Task.objects.get(id=id)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def task_create(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def task_edit(request, id):
    task = Task.objects.get(id=id)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def task_delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return Response({'success': 'task deleted successfully'}, status=status.HTTP_200_OK)
