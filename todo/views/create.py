from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from todo.forms import TaskModelForm


@login_required
def task_create_view(request):
    """
    Renders the task create view for authenticated users.

    This view is responsible for handling the creation of a new task.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: The rendered HTML response.
    """

    # Check if the request method is POST
    if request.method == "POST":
        # Create a form instance with the POST data
        form = TaskModelForm(request.POST)

        # Check if the form is valid
        if form.is_valid():
            # Save the form data to create a new task
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()

            # Display a success message
            messages.success(request, "Task Created")

            # Redirect the user to the home page
            return redirect("pages:home")
    else:
        # If the request method is not POST, create an empty form instance
        form = TaskModelForm()

    # Prepare the context data to be passed to the template
    context = {
        "title": "Create",
        "h1": "Create Task",
        "form": form,
    }

    # Render the create task page HTML with the provided template and context data
    return render(request, "todo/form.html", context)
