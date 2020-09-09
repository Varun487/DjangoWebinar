from django.db import models
from datetime import datetime

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    priority = models.IntegerField()

    def __str__(self):
        return self.title
