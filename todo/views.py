from django.shortcuts import render
from django.http import HttpResponse
from .models import Task


def home(request):
    return render(request, 'home.html')

def show_tasks(request):
    tasks = Task.objects.all()
    context= {"tasks" : tasks}
    return render(request,'tasks.html',context)