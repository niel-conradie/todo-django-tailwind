from django.test import TestCase
from django.urls import reverse_lazy, resolve

from pages.views import index_page_view


class IndexPageViewTests(TestCase):
    """
    The IndexPageViewTests class is a test case class for testing the functionality of an index page view.

    Parameters:
    - TestCase (class): TestCase is a class provided by Django for writing tests for your Django applications.

    Methods:
    - setUp(): Set up the test case by initializing the URL.
    - test_url_exists_at_correct_location(): Test if the URL exists at the correct location.
    - test_url_resolves(): Test whether the URL resolves to the correct view function.
    - test_correct_template_used(): Test whether the correct template is used when accessing the specified URL.
    """

    def setUp(self):
        """
        Set up the test case by initializing the URL.

        This function assumes that the specified URL renders the desired template.

        Parameters:
        - self: The instance of the test class.

        Returns:
        - None
        """

        # Initialize the URL using the reverse_lazy function from the Django framework
        self.url = reverse_lazy("pages:index")

    def test_url_exists_at_correct_location(self):
        """
        Test if the URL exists at the correct location.

        This function sends a GET request to the specified URL using the `client` object and checks if the response status code is equal to 200 using the `assertEqual` method.

        Parameters:
        - self: The instance of the test class.

        Return:
        - None
        """

        # Simulate a GET request by calling the `get` method of the `client` object
        response = self.client.get(self.url)

        # Check if the response status code is 200 using the `assertEqual` method
        self.assertEqual(response.status_code, 200)

    def test_url_resolves(self):
        """
        Test whether the URL resolves to the correct view function.

        This function uses the `resolve()` function to determine which view function is
        mapped to the given URL. It then asserts that the resolved view function is
        equal to the `index_page_view` function.

        Return Types:
        - None
        """

        # Resolve the URL to get the view function
        view = resolve("/")

        # Assert that the resolved view function is equal to the `index_page_view` function
        self.assertEqual(view.func.__name__, index_page_view.__name__)

    def test_correct_template_used(self):
        """
        Test whether the correct template is used when accessing the specified URL.

        This function sends an HTTP GET request to the URL specified by `self.url` and
        checks if the response uses the correct template.

        Parameters:
        - self: The instance of the test class.

        Returns:
        - None
        """

        # Simulate a GET request by calling the `get` method of the `client` object
        response = self.client.get(self.url)

        # Check if the response uses the correct template
        self.assertTemplateUsed(response, "pages/index.html")
