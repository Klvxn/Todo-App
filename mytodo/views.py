from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Todo
from .forms import TodoForm, EditTodoForm

# Create your views here.
def indexpage(request):
    return render(request, 'mytodo/indexpage.html')


def detailpage(request, pk):
    todo = Todo.objects.get(pk=pk)
    context = {'todo':todo}
    return render(request, 'mytodo/detailpage.html', context)


@login_required
def homepage(request):
    todo = Todo.objects.filter(user=request.user).order_by('-date_created')
    if request.POST.get('refresh'):
        for todos in todo:
            if request.POST.get('checked' + str(todos.pk)) == 'clicked':
                todos.completed = True
            else:
                todos.completed = False
            todos.save()
    todo_count = Todo.objects.filter(user=request.user, completed = False).count()
    context = {'todo':todo, 'todo_count':todo_count}
    return render(request, 'mytodo/homepage.html', context)


@login_required
def create_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
           todo = form.cleaned_data['todo']
           note = form.cleaned_data['note']
           user = request.user
           new_todo = Todo(todo=todo, note=note, completed=False, user=user)
           new_todo.save()
           return redirect(new_todo)
    else:
        form = TodoForm()
    context = {'form':form}
    return render(request, 'mytodo/create-todo.html', context)


@login_required
def edit_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    form = EditTodoForm()
    if todo.user == request.user:
        if request.method == "POST":
            form = EditTodoForm(instance=todo, data=request.POST)
            if form.is_valid():
                updated_todo = form.save(commit=False)
                updated_todo.save()
                return redirect(updated_todo)
        else:
            form = EditTodoForm(instance=todo)
    else:
        return HttpResponse('Where do you think you are going boss??')
    context = {'todo':todo, 'form':form}
    return render(request, 'mytodo/editpage.html', context)


@login_required
def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if todo.user == request.user:
        if request.method == 'POST':
            todo.delete()
            return redirect('mytodo:homepage')
    else:
        return HttpResponse('baddie')
    context = {'todo':todo}
    return render(request, 'mytodo/delete-todo.html', context)


@login_required
def completed_todos(request):
    todo = Todo.objects.filter(user=request.user, completed=True).order_by('-date_created')
    context = {'todos':todo}
    return render(request, 'mytodo/completed.html', context)


@login_required
def uncompleted_todos(request):
    todo = Todo.objects.filter(user=request.user, completed=False).order_by('-date_created')
    if request.POST.get('refresh'):
        for todos in todo:
            if request.POST.get('checked'+str(todos.pk)) == 'clicked':
                todos.completed = True
            todos.save()
    todo = Todo.objects.filter(user=request.user, completed=False).order_by('-date_created')
    context = {'todos':todo}
    return render(request, 'mytodo/uncompleted.html', context)