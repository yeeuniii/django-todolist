from django.db import models


# Create your models here.

class ToDoList(models.Model):
    objects = None
    content = models.CharField(max_length=100)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.content
