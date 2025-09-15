from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    

class TaskDetail(models.Model):
    task = models.OneToOneField(Task, on_delete=models.CASCADE, related_name='details')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(default=1,choices=[(1,'Low'),(2,'Medium'),(3,'High')])
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Detail for {self.task.title}"