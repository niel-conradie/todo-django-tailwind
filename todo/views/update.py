from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from todo.forms import TaskModelForm
from todo.models import TaskModel


@login_required
def task_update_view(request, slug, pk):
    """
    Update a task identified by its primary key.

    Parameters:
    - request (HttpRequest): The HTTP request object.
    - slug: The slug of the task.
    - pk: The primary key of the task.

    Returns:
    - HttpResponse: The rendered HTML response.

    Raises:
    - 404: If the task with the given pk does not exist.
    - login_required: If the user is not authenticated.
    """

    # Get the task with the given pk or 404 if it doesn't exist
    task = get_object_or_404(TaskModel, created_by=request.user, pk=pk)

    # Get the slug of the task's day
    slug = task.day.slug

    # Check if the request method is POST
    if request.method == "POST":
        # Create a form with the task's current data
        form = TaskModelForm(request.POST, instance=task)

        # Check if the form is valid
        if form.is_valid():
            # If the form is valid, save the updated task
            form.save()

            # Display a success message
            messages.success(request, "Task Updated")

            # Redirect the user to the home page
            return redirect("pages:home")
    else:
        # If the request method is not POST, create a form with the task's current data
        form = TaskModelForm(instance=task)

    # Prepare the context data to be passed to the template
    context = {
        "title": "Update",
        "h1": "Update Task",
        "form": form,
    }

    # Render the update task page HTML with the provided template and context data
    return render(request, "todo/form.html", context)
