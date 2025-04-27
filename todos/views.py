from django.shortcuts import render, get_object_or_404, redirect

from .models import Todo
from django.views import generic         #For class-based views like ListView
from django.http import HttpResponseRedirect         

#views.py - > allowing users to add, delete, update, and display to-do items.
          
class IndexView(generic.ListView):
    template_name = 'todos/index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):                       #It fetches all the to-do items from the Todo model
        """Return all the latest todos."""
        return Todo.objects.order_by('-created_at')

def add(request):                                 #add new todo-item to the list
    title = request.POST['title']  
    Todo.objects.create(title=title)

    return redirect('todos:index')

def delete(request, todo_id):             
    todo = get_object_or_404(Todo, pk=todo_id)     #It is used to fetch the item or show a 404 error if the item is not found.
    todo.delete()

    return redirect('todos:index')

def update(request, todo_id):                      #Handles marking a to-do item as completed or not completed.
    todo = get_object_or_404(Todo, pk=todo_id)
    isCompleted = request.POST.get('isCompleted', False)
    if isCompleted == 'on':
        isCompleted = True
    
    todo.isCompleted = isCompleted

    todo.save()
    return redirect('todos:index')