import pytest
from to_do_item.tests.factories.to_do_factory import ToDoItemFactory


@pytest.mark.django_db
def test_get_all_todos(client):
    to_do_item = ToDoItemFactory()

    response = client.get("/v1/to-do-items/")

    assert response.status_code == 200
    assert response.json() == [
        {
            "id": to_do_item.id,
            "name": "My Todo item",
            "description": "This is a description",
        }
    ]
