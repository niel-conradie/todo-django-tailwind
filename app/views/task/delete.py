from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from app.forms import DeleteModelForm
from app.models import TaskModel


@login_required
def task_delete_view(request, slug, pk):
    task = get_object_or_404(TaskModel, created_by=request.user, pk=pk)
    slug = task.day.title

    if request.method == "POST":
        form = DeleteModelForm(request.POST)

        if form.is_valid():
            task.delete()
            messages.success(request, "Task Deleted")
            return redirect("app:home")
    else:
        form = DeleteModelForm()

    context = {
        "form": form,
        "obj": task,
        "title": "Delete",
        "h1": "Delete Task",
    }
    return render(request, "app/delete.html", context)
