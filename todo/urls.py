from django.urls import path
from todo.views import AddTask, index, tasks,single_task

urlpatterns = [
    path('', index, name='index'), #the name of the URL is index
    path('tasks/', tasks, name='tasks'), #the name of the URL is topics
    path('tasks/<int:id>', single_task, name='single_task'),
    path('tasks/new_task', AddTask, name='add_task'),
]
