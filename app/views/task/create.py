from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from app.forms import TaskModelForm


@login_required
def task_create_view(request):
    if request.method == "POST":
        form = TaskModelForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            messages.success(request, "Task Created")
            return redirect("app:home")
    else:
        form = TaskModelForm()

    context = {
        "form": form,
        "title": "Create",
        "h1": "Create Task",
    }
    return render(request, "app/task_form.html", context)
