from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from app.models import TaskModel


@login_required
def task_reset_view(request):
    tasks = TaskModel.objects.filter(created_by=request.user)

    for task in tasks:
        if task.status == False:
            task.status = True
            task.save()
        else:
            pass

    messages.success(request, "Tasks Reset")

    return redirect("app:home")
