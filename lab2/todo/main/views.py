from django.shortcuts import render
from .models import Task
# Create your views here.

def todos(request):
    todos = Task.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})

def completed(request):
    todos = Task.objects.all()
    return render(request, 'todo/completed_todo_list.html', {'todos': todos})
