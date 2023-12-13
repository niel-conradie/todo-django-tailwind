from django.shortcuts import render


def index_page_view(request):
    """
    Render the index page view.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: The rendered HTML response.
    """

    # Define the template to be rendered
    template_name = "pages/index.html"

    # Render the index page HTML with the provided template
    return render(request, template_name)
