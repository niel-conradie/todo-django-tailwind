from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from todo.forms import DeleteModelForm
from todo.models import TaskModel


@login_required
def task_delete_view(request, slug, pk):
    task = get_object_or_404(TaskModel, created_by=request.user, pk=pk)
    slug = task.day.slug

    if request.method == "POST":
        form = DeleteModelForm(request.POST)

        if form.is_valid():
            task.delete()
            messages.success(request, "Task Deleted")
            return redirect("pages:home")
    else:
        form = DeleteModelForm()

    context = {
        "title": "Delete",
        "h1": "Delete Task",
        "form": form,
        "obj": task,
    }
    return render(request, "todo/delete.html", context)
