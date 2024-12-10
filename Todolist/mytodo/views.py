from django.shortcuts import render, redirect
from .models import Task
# Create your views here.

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/todo.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        task_title = request.POST.get('title')
        if task_title:
            Task.objects.create(title=task_title)
        return redirect('task_list')
    return render(request, 'tasks/todo.html')