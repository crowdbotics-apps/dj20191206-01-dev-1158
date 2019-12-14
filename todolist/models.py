from django.conf import settings
from django.db import models


class Todo(models.Model):
    "Generated Model"
    item_id = models.IntegerField()
    item_description = models.CharField(max_length=256,)
    is_complete = models.BooleanField()


# Create your models here.
