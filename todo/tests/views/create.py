from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse, resolve

from todo.views import task_create_view


CustomUser = get_user_model()


class TaskCreateViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user for testing
        cls.user = CustomUser.objects.create_user(
            username="user",
            email="user@email.com",
            password="testpassword1234",
        )

    def setUp(self):
        # Assuming this URL renders the template
        self.url = reverse("todo:create")

        # Create an client instance and login user
        self.client = Client()
        self.client.login(
            username="user",
            email="user@email.com",
            password="testpassword1234",
        )

    def test_template_rendering(self):
        # Simulate a GET request
        response = self.client.get(self.url)

        # Test if URL exists at correct location
        self.assertEqual(response.status_code, 200)

        # Test if form template is rendered
        self.assertTemplateUsed(response, "todo/form.html")

        # Test if view URL resolves
        view = resolve("/task/create/")
        self.assertEqual(view.func.__name__, task_create_view.__name__)

        # Test if the rendered HTML contains content
        self.assertContains(response, "Create Task")

    def test_template_context(self):
        # Simulate a GET request
        response = self.client.get(self.url)

        # Test if template context is available
        self.assertIn("title", response.context)
        self.assertIn("h1", response.context)
        self.assertIn("form", response.context)
