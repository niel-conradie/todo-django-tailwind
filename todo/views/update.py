from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from todo.forms import TaskModelForm
from todo.models import TaskModel


@login_required
def task_update_view(request, slug, pk):
    task = get_object_or_404(TaskModel, created_by=request.user, pk=pk)
    slug = task.day.slug

    if request.method == "POST":
        form = TaskModelForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            messages.success(request, "Task Updated")
            return redirect("pages:home")
    else:
        form = TaskModelForm(instance=task)

    context = {
        "form": form,
        "title": "Update",
        "h1": "Update Task",
    }
    return render(request, "todo/form.html", context)
