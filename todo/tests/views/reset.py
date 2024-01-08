from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse_lazy, resolve

from todo.views import task_reset_view


CustomUser = get_user_model()


class TaskResetViewTests(TestCase):
    """
    The TaskResetViewTests class is a test case class for testing the functionality of an task reset view.

    Parameters:
    - TestCase (class): TestCase is a class provided by Django for writing tests for your Django applications.

    Methods:
    - setUpTestData(cls): Set up the test data for the class.
    - setUp(self): Set up the test environment before running the test cases.
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
        self.url = reverse_lazy("todo:reset")

        # Create an client instance and login user
        self.client = Client()
        self.client.login(
            username="user",
            email="user@email.com",
            password="testpassword1234",
        )
