from django.shortcuts import render
from .models import Task
from .forms import TaskForm

def home(request):
    return render(request, 'home.html')

def show_tasks(request):
    tasks = Task.objects.all()
    context= {"tasks" : tasks}
    return render(request,'tasks.html',context)

def create_task(request):
    form = TaskForm()
    context = {"form" : form}
    if(request.POST):
        return render(request,'home.html')
    else:
        return render(request, 'create_task.html',context)