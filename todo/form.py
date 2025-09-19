from django import forms

class TaskForm(forms.Form):
    task = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    priority = forms.IntegerField(min_value=1, max_value=3, initial=1)
    completed = forms.BooleanField(required=False, initial=False)

