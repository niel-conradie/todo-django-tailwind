from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse_lazy, resolve

from todo.views import task_create_view


CustomUser = get_user_model()


class TaskCreateViewTests(TestCase):
    """
    The TaskCreateViewTests class is a test case class for testing the functionality of an task create view.

    Parameters:
    - TestCase (class): TestCase is a class provided by Django for writing tests for your Django applications.

    Methods:
    - setUpTestData(cls): Set up the test data for the class.
    - setUp(self): Set up the test environment before running the test cases.
    - test_url_exists_at_correct_location(self): Test if the URL exists at the correct location.
    - test_url_resolves(self): Test whether the URL resolves to the correct view function.
    - test_correct_template_used(self): Test whether the correct template is used when accessing the specified URL.
    - test_correct_template_html(self): Test the correctness of the HTML template.
    - test_correct_template_context(self): Test the correctness of the template context.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up test data for the test case.

        This method is a class method and is used to set up the necessary data for the test case.
        It creates a user for testing purposes using the `CustomUser` model and sets the username, email, and password.

        Parameters:
        - cls (class): The class object.

        Returns:
        - None
        """

        # Create a user for testing
        cls.user = CustomUser.objects.create_user(
            username="user",
            email="user@email.com",
            password="testpassword1234",
        )

    def setUp(self):
        """
        Set up the test environment before running the test cases.

        It initializes the URL using the reverse_lazy function from the Django framework.
        It also creates a client instance and logs in a user with a specified username, email, and password.

        Parameters:
        - self: The instance of the test class.

        Returns:
        - None
        """

        # Initialize the URL using the reverse_lazy function from the Django framework
        self.url = reverse_lazy("todo:create")

        # Create an client instance and login user
        self.client = Client()
        self.client.login(
            username="user",
            email="user@email.com",
            password="testpassword1234",
        )

    def test_url_exists_at_correct_location(self):
        """
        Test if the URL exists at the correct location.

        This function simulates a GET request to the URL using the `client` object.
        It then checks if the response status code is equal to 200 using the `assertEqual` method.

        Parameters:
        - self: The instance of the test class.

        Returns:
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
        equal to the `task_create_view` function.

        Parameters:
        - self: The instance of the test class.

        Return Types:
        - None
        """

        # Resolve the URL to get the view function
        view = resolve("/task/create/")

        # Assert that the resolved view function is equal to the `task_create_view` function
        self.assertEqual(view.func.__name__, task_create_view.__name__)

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
        self.assertTemplateUsed(response, "todo/form.html")

    def test_correct_template_html(self):
        """
        Test the correctness of the HTML template.

        This function simulates a GET request by calling the `get` method of the `client` object.
        It then asserts that the response contains the following strings: "Create Task".

        Parameters:
        - self: The instance of the test class.

        Return Types:
        - None
        """

        # Simulate a GET request by calling the `get` method of the `client` object
        response = self.client.get(self.url)

        # Test if template html is accurate
        self.assertContains(response, "Create Task")

    def test_correct_template_context(self):
        """
        Test the correctness of the template context.

        It sends a GET request to a specific URL and then checks if the expected variables (title, h1, form)
        are present in the response context.

        Parameters:
        - self: The instance of the test class.

        Return Types:
        - None
        """

        # Simulate a GET request by calling the `get` method of the `client` object
        response = self.client.get(self.url)

        # Test if template context data is accurate
        self.assertIn("title", response.context)
        self.assertIn("h1", response.context)
        self.assertIn("form", response.context)
