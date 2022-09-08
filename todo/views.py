from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def show_tasks(request):
    tasks = Task.objects.all()
    context= {"tasks" : tasks}
    return render(request,'tasks.html',context)

def show_task(request,id):
    task = Task.objects.filter(pk=id).first()
    context = {"task" : task}
    return render(request,'task.html',context)

def create_task(request):
    form = TaskForm()
    error = ''
    
    if request.method == 'POST':
        
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
        else :
            error = 'Invalid Data'
            context = {"form" : form, "error" : error}
            return render(request,'create_task.html', context)
            
    else:
        context = {'form' : form}
        return render(request,'create_task.html', context)