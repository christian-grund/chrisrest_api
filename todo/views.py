from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from django.core import serializers

from todo.serializers import TodoSerializer
from todo.models import Todo


class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Todo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer
    permission_classes = [] # permissions.IsAuthenticated

    def create(self, request):
        todo = Todo.objects.create(title= request.POST.get('title', ''), 
                                  description= request.POST.get('description', ''),
                                  user= request.user,
                                )
        serialized_obj = serializers.serialize('json', [todo, ]) 
        return HttpResponse(serialized_obj, content_type='application/json')