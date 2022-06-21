from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EditTodoForm, TodoForm
from .models import Todo


# Create your views here.
def indexpage(request):
    return render(request, "mytodo/indexpage.html")


@login_required
def detailpage(request, pk):
    todo = Todo.objects.get(pk=pk)
    context = {"todo": todo}
    return render(request, "mytodo/detailpage.html", context)


@login_required
def homepage(request):
    todo = Todo.objects.filter(user=request.user)
    if request.POST.get("refresh"):
        for todos in todo:
            if request.POST.get("checked" + str(todos.pk)) == "clicked":
                todos.completed = True
            else:
                todos.completed = False
            todos.save()
    todo_count = Todo.objects.filter(user=request.user, completed=False).count()
    context = {"todo": todo, "todo_count": todo_count}
    return render(request, "mytodo/homepage.html", context)


@login_required
def create_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.cleaned_data["todo"]
            note = form.cleaned_data["note"]
            user = request.user
            new_todo = Todo(todo=todo, note=note, completed=False, user=user)
            new_todo.save()
            return redirect(new_todo)
    else:
        form = TodoForm()
    context = {"form": form}
    return render(request, "mytodo/add-todo.html", context)


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
        return HttpResponseForbidden("<h1> (ERROR!) Access denied.</h1>")
    context = {"todo": todo, "form": form}
    return render(request, "mytodo/editpage.html", context)


@login_required
def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if todo.user == request.user:
        if request.method == "POST":
            todo.delete()
            return redirect("mytodo:homepage")
    else:
        return HttpResponseForbidden("<h1> (ERROR!) Request denied.</h1>")
    context = {"todo": todo}
    return render(request, "mytodo/delete-todo.html", context)


@login_required
def completed_todos(request):
    todo = Todo.objects.filter(user=request.user, completed=True)
    context = {"todos": todo}
    return render(request, "mytodo/completed.html", context)


@login_required
def incomplete_todos(request):
    todo = Todo.objects.filter(user=request.user, completed=False)
    if request.POST.get("refresh"):
        for todos in todo:
            if request.POST.get("checked" + str(todos.pk)) == "clicked":
                todos.completed = True
            todos.save()
    todo = Todo.objects.filter(user=request.user, completed=False)
    context = {"todos": todo}
    return render(request, "mytodo/incompleted.html", context)
