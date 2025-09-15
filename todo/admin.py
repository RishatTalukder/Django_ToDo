from django.contrib import admin

# Register your models here.
from .models import Task, TaskDetail

admin.site.register(Task)
admin.site.register(TaskDetail)