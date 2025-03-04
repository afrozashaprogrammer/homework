from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from .models import *
from .pagination import *

# Create your views here.
@api_view(['GET'])
def index(request):
    person1 = {
        "name": "Raisha",
        "age": 22,
        "ia_married": "Flase"
    }
    person2 = {
        "name": "Ayesha",
        "age": 10,
        "is_married": "Flase"
    }
    person_list = [person1, person2]
    return Response(person_list)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def todo_list(request):
    if request.method == 'GET':
        todos = Todo.objects.all()

        paginator = TodoPagination()
        page = paginator.paginate_queryset(todos, request)
        if page is not None:
            serializer = TodoListSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        
        serializer = TodoListSerializer(todos, many=True)
        return Response(serializer.data)
    

    elif request.method == 'POST':
        data = request.data
        serializer = TodoCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BED_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
def todo_detail(request, id):
    todo = get_object_or_404(Todo, id=id)

    if request.method == 'GET':
        serializer = TodoDetailSerializer(todo)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        data = request.data
        serializer = TodoDetailSerializer(todo, data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    elif request.method == 'DELETE':
        todo.delete()
        message = {"success": "Todo has been deleted successfully"}
        return Response(message, status=status.HTTP_204_NO_CONTENT)

