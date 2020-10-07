import factory
from to_do_item.models import ToDoItem
from to_do_item.tests.factories.reporter_factory import ReporterFactory
from factory.django import DjangoModelFactory


class ToDoItemFactory(DjangoModelFactory):
    class Meta:
        model = ToDoItem

    name = "My Todo item"  # Default value for the `name` field
    description = "This is a description"  # Default value for the `description` field
    reporter = factory.SubFactory(ReporterFactory)
