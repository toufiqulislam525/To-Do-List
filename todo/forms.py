# Model Forms

from django.forms import ModelForm
from django import forms
from .models import Task
from django.contrib.admin.widgets import AdminDateWidget,AdminSplitDateTime

class TaskForm(ModelForm):
    completed = forms.SplitDateTimeField(widget=AdminSplitDateTime())
    class Meta:
        model = Task
        fields = '__all__'
        
        
        