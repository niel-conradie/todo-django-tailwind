from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from todo.models import TaskModel


@login_required
def home_page_view(request):
    """
    Renders the home page view for authenticated users.

    Retrieves all tasks created by the current user from the TaskModel model.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: The rendered HTML response.
    """

    # Retrieve all tasks created by the current user
    tasks = TaskModel.objects.filter(created_by=request.user).order_by(
        "-status",
        "time_start",
        "time_end",
    )

    # Define the template to be rendered
    template_name = "pages/home.html"

    # Prepare the context data to be passed to the template
    context = {
        "tasks": tasks,
    }

    # Render the home page HTML with the provided template and context data
    return render(request, template_name, context)
