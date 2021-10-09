from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Todo

# Create your views here.
def signin(request):
    return HttpResponse('Sign in')

def signup(request):
    return HttpResponse('<h1>Sign up</h1>')

def home(request):
    todos = Todo.objects.all()
    data = {
        'todos': todos
    }
    return render(request, 'app/home.html', data)

def todo_form(request):
    if request.method == 'POST':
        print(request.POST)
        title = request.POST['title']
        description = request.POST['description']
        print("Data: ", title, description)
        todo = Todo()
        todo.title = title
        todo.descripction = description
        todo.save()
    return render(request, 'app/todo_form.html')

def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect(to='home')