from django.db import models


class ToDoItem(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=255)
