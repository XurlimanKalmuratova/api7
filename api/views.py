from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import *
from rest_framework.response  import Response
from .permission import UserPermission, UserDetailPermission, ProjectPermission, ProjectDetailPermission, TaskPermission, TaskDetailPermission


from app.models import CustomUser
from .serializers import UserSerializer

@api_view(['GET', 'POST'])
@permission_classes([UserPermission])
def user(request):
    if request.method == 'GET':
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([UserDetailPermission])
def user_detail(request, pk):
    user = CustomUser.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'DELETE':
        user.delete() 
        return Response (status=HTTP_204_NO_CONTENT)



from app.models import Task
from .serializers import TaskSerializer

@api_view(['GET'])
@permission_classes([TaskPermission])
def task(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TaskSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([TaskDetailPermission])
def task_detail(request, pk):
    user = Task.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = TaskSerializer(request.data)
        if serializer.is_valid():
            serializer.save()    
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'DELETE':
        user.delete() 
        return Response (status=HTTP_204_NO_CONTENT)
    

from app.models import Project
from .serializers import ProjectSerializer

@api_view(['GET'])
@permission_classes([ProjectPermission])
def project(request):
    if request.method == 'GET':
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ProjectSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([ProjectDetailPermission])
def project_detail(request, pk):
    user = Project.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = ProjectSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'DELETE':
        user.delete() 
        return Response (status=HTTP_204_NO_CONTENT)

