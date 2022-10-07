from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from .forms import EditTodoForm, TodoForm
from .helpers import HtmxRedirect
from .models import Todo


# Create your views here.
def indexpage(request):
    return render(request, "mytodo/indexpage.html")


@login_required
def homepage(request):
    todos = Todo.objects.filter(user=request.user)
    completed_todos = todos.filter(completed=True)
    incomplete_todos = todos.filter(completed=False)

    if request.method == "POST":
        data = request.POST.copy()
        data.pop("csrfmiddlewaretoken")
        for todo_id, value in data.items():
            if value == "check":
                todos.filter(id=todo_id).update(completed=True)
            else:
                todos.filter(id=todo_id).update(completed=False)
            return HtmxRedirect(reverse("mytodo:homepage"))

    elif request.method == "DELETE":
        completed_todos.delete()
        return HtmxRedirect(reverse("mytodo:homepage"), 204)

    todo_count = incomplete_todos.count()
    context = {
        "completed_todos": completed_todos,
        "incomplete_todos": incomplete_todos,
        "todo_count": todo_count
    }
    return render(request, "mytodo/homepage.html", context)


@login_required
def detailpage(request, pk):
    todo = get_object_or_404(Todo, user=request.user, pk=pk)
    if request.method == "POST":
        data = request.POST.copy()
        for value in data.values():
            if value == "check":
                todo.completed = True
            else:
                todo.completed = False
            todo.save()
            return HtmxRedirect(todo.get_absolute_url())

    context = {"todo": todo}
    return render(request, "mytodo/detailpage.html", context)


@login_required
def create_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Todo.objects.create(
                todo=data["todo"], note=data["note"], completed=False, user=request.user
            )
            return HtmxRedirect(reverse("mytodo:homepage"), 201)

    form = TodoForm()
    context = {"form": form}
    return render(request, "mytodo/add-todo.html", context)


@login_required
def edit_todo(request, pk):
    todo = get_object_or_404(Todo, user=request.user, pk=pk)
    form = EditTodoForm()
    if todo.user == request.user:
        if request.method == "POST":
            form = EditTodoForm(instance=todo, data=request.POST)
            if form.is_valid():
                updated_todo = form.save(commit=False)
                updated_todo.save()
                return HtmxRedirect(todo.get_absolute_url())

        form = EditTodoForm(instance=todo)
        context = {"todo": todo, "form": form}
        return render(request, "mytodo/editpage.html", context)

    return HttpResponseForbidden("<h1> (ERROR!) Access denied.</h1>")


@login_required
@require_http_methods(["DELETE", "POST"])
def delete_todo(request, pk):
    todo = get_object_or_404(Todo, user=request.user, pk=pk)
    if todo.user == request.user:
        todo.delete()
        return HtmxRedirect(reverse("mytodo:homepage"), 204)

    return HttpResponseForbidden("<h1> (ERROR!) Request denied.</h1>")
