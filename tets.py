from todo.models import Task

task = Task.objects.first()

print(task)