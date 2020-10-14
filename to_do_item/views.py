from rest_framework import viewsets
from to_do_item.models import ToDoItem
from to_do_item.serializers import ToDoItemSerializer


class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
