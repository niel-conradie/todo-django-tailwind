from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from todo.forms import DeleteModelForm
from todo.models import TaskModel


@login_required
def task_delete_view(request, slug, pk):
    """
    Delete a task identified by its primary key.

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
        # Create a form instance with the POST data
        form = DeleteModelForm(request.POST)

        # Check if the form is valid
        if form.is_valid():
            # If the form is valid, delete the task
            task.delete()

            # Display a success message
            messages.success(request, "Task Deleted")

            # Redirect the user to the home page
            return redirect("pages:home")
    else:
        # If the request method is not POST, create an empty form instance
        form = DeleteModelForm()

    # Prepare the context data to be passed to the template
    context = {
        "title": "Delete",
        "h1": "Delete Task",
        "form": form,
        "obj": task,
    }

    # Render the delete task page HTML with the provided template and context data
    return render(request, "todo/delete.html", context)
