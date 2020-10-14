from to_do_item.models import ToDoItem
from factory.django import DjangoModelFactory


class ToDoItemFactory(DjangoModelFactory):
    class Meta:
        model = ToDoItem

    name = "My Todo item"  # Default value for the `name` field
    description = "This is a description"  # Default value for the `description` field
