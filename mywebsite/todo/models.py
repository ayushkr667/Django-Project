from django.db import models

# Create your models here.

class Todo(models.Model):
    complete = models.BooleanField(default=False)
    todotext = models.TextField()

    def __str__(self):
        return self.todotext
