from django.contrib.auth import get_user_model
from django.test import TestCase

from datetime import time

from todo.models import DayModel, TaskModel


CustomUser = get_user_model()


class TaskModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
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
        self.assertEqual(self.task.title, "Task Title")
        self.assertEqual(self.task.day.title, "monday")
        self.assertEqual(self.task.day.slug, "monday")
        self.assertEqual(self.task.time_start, time(hour=9))
        self.assertEqual(self.task.time_end, time(hour=10))
        self.assertEqual(self.task.created_by, self.user)
        self.assertEqual(self.task.status, True)  # Ensure default status is True

    def test_task_status_change(self):
        self.task.status = False
        self.task.save()
        updated_task = TaskModel.objects.get(pk=self.task.pk)
        self.assertEqual(updated_task.status, False)  # Ensure status is False
