from rest_framework import serializers
from to_do_item.models import ToDoItem


class ToDoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = "__all__"
