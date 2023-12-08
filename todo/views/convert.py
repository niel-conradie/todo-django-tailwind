from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from todo.models import TaskModel


@login_required
def task_convert_view(request, pk):
    task = get_object_or_404(TaskModel, created_by=request.user, pk=pk)

    if task.status == True:
        task.status = False
        messages.success(request, "Task Completed")
    else:
        task.status = True
        messages.warning(request, "Task Incomplete")

    task.save()
    return redirect("pages:home")
