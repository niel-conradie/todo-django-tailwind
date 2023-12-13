from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse_lazy, resolve

from datetime import time

from pages.views import home_page_view
from todo.models import DayModel, TaskModel


CustomUser = get_user_model()


class HomePageViewTests(TestCase):
    """
    The HomePageViewTests class is a test case class for testing the functionality of an home page view.

    Parameters:
    - TestCase (class): TestCase is a class provided by Django for writing tests for your Django applications.

    Methods:
    - setUpTestData(): Set up the test data for the class.
    - setUp(): Set up the test environment before running the test cases.
    - test_url_exists_at_correct_location(): Test if the URL exists at the correct location.
    - test_url_resolves(): Test whether the URL resolves to the correct view function.
    - test_correct_template_used(): Test whether the correct template is used when accessing the specified URL.
    - test_correct_template_html(): Test the correctness of the HTML template.
    - test_correct_template_context(): Test the correctness of the template context.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up test data for the test case.

        This method is a class method and is used to set up the necessary data for the test case.
        It creates a user for testing purposes using the `CustomUser` model and sets the username, email, and password.
        It also creates a `DayModel` object with a title and slug, and a `TaskModel` object with a
        title, day, start time, end time, and created by.

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

        # Create DayModel data for testing
        cls.day = DayModel.objects.create(title="monday", slug="monday")

        # Create TaskModel data for testing
        cls.task = TaskModel.objects.create(
            title="Task Title",
            day=cls.day,
            time_start=time(hour=9),
            time_end=time(hour=10),
            created_by=cls.user,
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
        self.url = reverse_lazy("pages:home")

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
        equal to the `home_page_view` function.

        Parameters:
        - self: The instance of the test class.

        Return Types:
        - None
        """

        # Resolve the URL to get the view function
        view = resolve("/home/")

        # Assert that the resolved view function is equal to the `home_page_view` function
        self.assertEqual(view.func.__name__, home_page_view.__name__)

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
        self.assertTemplateUsed(response, "pages/home.html")

    def test_correct_template_html(self):
        """
        Test the correctness of the HTML template.

        This function simulates a GET request by calling the `get` method of the `client` object.
        It then asserts that the response contains the following strings: "Task Title", "09:00", and "10:00".

        Parameters:
        - self: The instance of the test class.

        Return Types:
        - None
        """

        # Simulate a GET request by calling the `get` method of the `client` object
        response = self.client.get(self.url)

        self.assertContains(response, "Task Title")
        self.assertContains(response, "09:00")
        self.assertContains(response, "10:00")

    def test_correct_template_context(self):
        """
        Test the correctness of the template context.

        It sends a GET request to a specific URL and then checks if the expected variables (tasks, task)
        are present in the response context.

        Parameters:
        - self: The instance of the test class.

        Return Types:
        - None
        """

        # Simulate a GET request by calling the `get` method of the `client` object
        response = self.client.get(self.url)

        # Test if template context is available
        self.assertIn("task", response.context)
        task_in_context = response.context["task"]

        # Test if template context data is accurate
        self.assertEqual(task_in_context.title, "Task Title")
        self.assertEqual(task_in_context.day.title, "monday")
        self.assertEqual(task_in_context.time_start, time(hour=9))
        self.assertEqual(task_in_context.time_end, time(hour=10))
        self.assertEqual(task_in_context.created_by, self.user)
        self.assertEqual(task_in_context.status, True)
