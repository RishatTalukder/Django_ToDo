from django import forms

from todo.models import TaskDetail

class TaskForm(forms.Form):
    task = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea, required=False)
    priority = forms.IntegerField(min_value=1, max_value=3, initial=1)
    completed = forms.BooleanField(required=False, initial=False)

class TaskDetailForm(forms.ModelForm):
    class Meta:
        model = TaskDetail
        fields = ['description', 'priority', 'completed']