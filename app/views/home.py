from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from app.models import TaskModel


@login_required
def home_page_view(request):
    tasks = TaskModel.objects.filter(created_by=request.user).order_by(
        "-status",
        "time_start",
        "time_end",
    )

    context = {
        "tasks": tasks,
    }
    return render(request, "app/home.html", context)
