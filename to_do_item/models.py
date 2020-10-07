from django.db import models
from django.conf import settings


class ToDoItem(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=255)
    reporter = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )
