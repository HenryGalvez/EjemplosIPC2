from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Todo
import requests

URL = "http://localhost:4000/api/"

# Create your views here.
def signin(request):
    return HttpResponse('Sign in')

def signup(request):
    return HttpResponse('<h1>Sign up</h1>')

def home(request):
    #todos = Todo.objects.all()
    res = requests.get(URL+"todo/")
    todos = []
    if res.status_code == 200:
        todos = res.json()["data"]
    data = {
        'todos': todos
    }
    return render(request, 'app/home.html', data)

def todo_form(request):
    data = {
        "todo": {
            "id": 0,
            "title": "",
            "description": ""
        },
        "action": "",
        "update": False
    }
    if request.method == 'POST':
        print(request.POST)
        #title = request.POST['title']
        #description = request.POST['description']
        #print("Data: ", title, description)
        #todo = Todo()
        #todo.title = title
        #todo.descripction = description
        #todo.save()
        res = requests.post(URL+'todo/insert', json=request.POST)
    return render(request, 'app/todo_form.html')

def update_todo(request, id):
    if request.method == 'POST':
        print(request.POST)
        #title = request.POST['title']
        #description = request.POST['description']
        #print("Data: ", title, description)
        #todo = Todo()
        #todo.title = title
        #todo.descripction = description
        #todo.save()
        res = requests.put(URL+'todo/update', params={"id": id}, json=request.POST)
    res = requests.get(URL+"todo/getById", params={"id": id})
    todo = res.json()["data"]
    data = {
        "todo": todo,
        "action": todo["id"],
        "update": True
    }
    return render(request, 'app/todo_form.html', data)

def delete_todo(request, id):
    #todo = get_object_or_404(Todo, id=id)
    #todo.delete()
    res = requests.delete(URL+"todo/delete",params={"id": id})
    return redirect(to='home')