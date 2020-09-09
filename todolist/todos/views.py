from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()

    # to add variables
    context = {
        'todos': todos
    }

    return render(request, 'index.html', context)

def add(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        priority = request.POST['priority']

        print('title: ', title)
        print('content: ', content)
        print('priority: ', priority)

        todo = Todo(title=title, content=content, priority=priority)
        todo.save()

        return redirect('/todos')

def delete(request, id):
    if request.method == 'POST':

        todo = Todo.objects.get(id=id)
        todo.delete()

    return redirect('/todos')
