from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from django.core import serializers
# Create your views here.


def index(request):
    data = Task.objects.all()
    data = serializers.serialize('json', data)
    return HttpResponse(data, content_type='application/json')