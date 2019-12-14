from rest_framework import authentication
from todolist.models import Todo
from .serializers import TodoSerializer
from rest_framework import viewsets


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Todo.objects.all()
