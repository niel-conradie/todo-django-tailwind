from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from todo.models import TaskModel


@login_required
def task_reset_view(request):
    """
    Reset status of all tasks.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: The rendered HTML response.

    Raises:
    - login_required: If the user is not authenticated.
    """

    # Retrieve all tasks created by the current user
    tasks = TaskModel.objects.filter(created_by=request.user)

    # Iterate over each task
    for task in tasks:
        # Set the status of the task to True if it is currently False
        if task.status == False:
            task.status = True
            # Save the updated task
            task.save()
        else:
            pass

    # Display a success message
    messages.success(request, "Tasks Reset")

    # Redirect the user to the home page
    return redirect("pages:home")
