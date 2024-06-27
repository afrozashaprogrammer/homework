from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
