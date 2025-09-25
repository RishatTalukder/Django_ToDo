from django.urls import path
from todo.views import AddTask, DeleteTask, UpdateTaskDetail, index, tasks,single_task

urlpatterns = [
    path('', index, name='index'), 
    path('tasks/', tasks, name='tasks'), 
    path('tasks/<int:id>', single_task, name='single_task'),
    path('tasks/new_task', AddTask, name='add_task'),
    path('tasks/update_taskdetail/<int:id>', UpdateTaskDetail, name='update_taskdetail'),
    path('tasks/delete_task/<int:id>', DeleteTask, name='delete_task')
]
