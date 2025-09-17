from django.shortcuts import render
from django.http import HttpResponse
from .models import Task, TaskDetail
from django.core import serializers
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
    taskdetail = TaskDetail.objects.get(task=task)
    # taskdetail = task.details
    context = {'task': task, 'taskdetail': taskdetail}
    return render(request, 'todo/single_task.html', context)