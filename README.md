# To Do List Application
### Endpoints
- `GET - /v1/to-do-items/`: List the To Do items
- `POST - /v1/to-do-items/`: Create a To Do item 
- `GET - /v1/to-do-items/<id>/`: Retrieve a To Do item
- `PUT - /v1/to-do-items/<id>/`:  Update a To Do item
- `DELETE - /v1/to-do-items/<id>/`:  Delete a To Do item

## Requirements
- python 3
- poetry

If poetry is not installed, you can run this command
```
python -m pip install poetry
```

## Setup
##### Enter virtual environment
```
poetry shell
```
##### Install the dependencies
```
poetry install
```
##### Migrate the database
```
python manage.py migrate
```
##### Start the application
```
python manage.py runserver
```

## Running the tests
```
pytest .
```