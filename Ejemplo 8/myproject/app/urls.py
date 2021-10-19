from django.urls import path
from .views import home, signin, signup, todo_form, delete_todo, update_todo

urlpatterns = [
    path('', home, name='home'),
    path('todo_form', todo_form, name='todo_form'),
    path('delete_todo/<id>', delete_todo, name='delete_todo'),
    path('update_todo/<id>', update_todo, name='update_todo'),
    path('signup', signup, name='signup'),
    path('signin', signin, name='signin'),
]
