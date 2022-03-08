from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=500)
    created_date = models.DateField()
    due_on = models.DateField()
    owner = models.CharField(max_length=500)
    mark = models.BooleanField()

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
