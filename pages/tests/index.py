from django.test import SimpleTestCase
from django.urls import reverse, resolve

from pages.views import IndexPageView


class IndexPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("pages:index")
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, "pages/index.html")

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, "Test")

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_homepage_url_resolves_indexpageview(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, IndexPageView.as_view().__name__)