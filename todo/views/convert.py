from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from todo.models import TaskModel


@login_required
def task_convert_view(request, pk):
    """
    Convert a task identified by its primary key.

    Parameters:
    - request (HttpRequest): The HTTP request object.
    - pk: The primary key of the task.

    Returns:
    - HttpResponse: The rendered HTML response.

    Raises:
    - 404: If the task with the given pk does not exist.
    - login_required: If the user is not authenticated.
    """

    # Get the task with the given pk or 404 if it doesn't exist
    task = get_object_or_404(TaskModel, created_by=request.user, pk=pk)

    # Toggle the status of the task
    if task.status == True:
        task.status = False

        # Display a success message
        messages.success(request, "Task Completed")
    else:
        task.status = True

        # Display a warning message
        messages.warning(request, "Task Incomplete")

    # Save the updated task
    task.save()

    # Redirect the user to the home page
    return redirect("pages:home")
