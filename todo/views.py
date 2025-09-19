from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Task, TaskDetail
from django.core import serializers
from .form import TaskForm
# Create your views here.


# def index(request):
#     data = Task.objects.all()
#     data = serializers.serialize('json', data)
#     return HttpResponse(data, content_type='application/json')


def index(request):
    return render(request, 'todo/index.html')


def tasks(request):
    data = Task.objects.order_by('-created_at')
    context = {'tasks': data}
    return render(request, 'todo/tasks.html', context)

def single_task(request, id):
    task = Task.objects.get(id=id)
    try:
        taskdetail = TaskDetail.objects.get(task=task)
    except:
        taskdetail = None
    # taskdetail = TaskDetail.objects.get(task=task)
    # taskdetail = task.details
    context = {'task': task, 'taskdetail': taskdetail}
    return render(request, 'todo/single_task.html', context)

def AddTask(request):
    print(request)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['task']
            description = form.cleaned_data['description']
            priority = form.cleaned_data['priority']
            completed = form.cleaned_data['completed']
            task = Task(title=title)
            task.save()
            taskdetail = TaskDetail(task=task, description=description, priority=priority, completed=completed)
            taskdetail.save()
            return redirect('tasks')
    else:
        form = TaskForm()
    context = {'form': form}
    return render(request, 'todo/add_task.html', context)