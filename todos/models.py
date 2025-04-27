
from django.db import models                    #all the built-in fields

class Todo(models.Model):
    title = models.CharField(max_length=100)                    
    created_at = models.DateTimeField('Created', auto_now_add=True)     #store the date and time when the task was created.
    update_at = models.DateTimeField('Updated', auto_now=True)          # updates the timestamp every time the task is updated.
    isCompleted = models.BooleanField(default=False)                    #task is incomplete by default

    def __str__(self):
        return self.title
       
