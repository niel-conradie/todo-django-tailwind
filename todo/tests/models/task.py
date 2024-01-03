from django.contrib.auth import get_user_model
from django.test import TestCase

from datetime import time

from todo.models import DayModel, TaskModel


CustomUser = get_user_model()


class TaskModelTests(TestCase):
    """
    The TaskModelTests class is a test case class that is used for writing tests for the TaskModel model.

    Parameters:
    - TestCase (class): TestCase is a class provided by Django for writing tests for your Django applications.

    Methods:
    - setUpTestData(cls): Set up the test data for the class.
    - test_create_task(self): Test the creation of the task of the day.
    - test_change_task_status(self): Test the status change of a task.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up the test data for the class.

        This method creates a user for testing and sets it as the class attribute `user`. It also creates a `DayModel` object and sets it as the class attribute `day`. Additionally, it creates a `TaskModel` object and sets it as the class attribute `task`. The `TaskModel` object is associated with the `DayModel` object and the user created for testing.

        Parameters:
        - cls: The class object.

        Returns:
        - None
        """

        # Create a user for testing
        cls.user = CustomUser.objects.create_user(
            username="testuser",
            email="testuser@email.com",
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

    def test_create_task(self):
        """
        Test the creation of the task of the day.

        This function asserts that the task is created correctly by checking various attributes of the task object.

        Parameters:
        - self: The instance of the test class.

        Returns:
        - None
        """

        # Assert that the title of the task is "Task Title"
        self.assertEqual(self.task.title, "Task Title")

        # Assert that the title of the day associated with the task is "monday"
        self.assertEqual(self.task.day.title, "monday")

        # Assert that the slug of the day associated with the task is "monday"
        self.assertEqual(self.task.day.slug, "monday")

        # Assert that the start time of the task is 9 AM
        self.assertEqual(self.task.time_start, time(hour=9))

        # Assert that the end time of the task is 10 AM
        self.assertEqual(self.task.time_end, time(hour=10))

        # Assert that the creator of the task is the user instance
        self.assertEqual(self.task.created_by, self.user)

        # Assert that the status of the task is True
        self.assertEqual(self.task.status, True)

    def test_change_task_status(self):
        """
        Test the status change of a task.

        This function is used to test the status change of a task. It sets the status of the task to False, saves the task,
        retrieves the updated task from the database, and asserts that the status of the updated task is False.

        Parameters:
            self (TestCase): The instance of the test case class.

        Returns:
            None
        """

        # Set the status of the task to False
        self.task.status = False

        # Save the task
        self.task.save()

        # Retrieve the updated task from the database
        updated_task = TaskModel.objects.get(pk=self.task.pk)

        # Assert that the status of the updated task is False
        self.assertEqual(updated_task.status, False)
