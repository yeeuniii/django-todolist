from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from todolist.models import ToDoList


# Create your views here.

def todolist(request):
    if request.method == 'POST':
        todo = ToDoList()
        todo.content = request.POST.get('todo_input')
        todo.save()
        return HttpResponseRedirect(reverse('todolist:index'))
    todos = ToDoList.objects.all()
    return render(request, 'todolist/index.html', context={'todos': todos})
