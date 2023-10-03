from django.test import SimpleTestCase
from django.urls import reverse, resolve

from pages.views import PrivacyPageView


class PrivacyPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("pages:privacy")
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_privacypage_template(self):
        self.assertTemplateUsed(self.response, "pages/privacy.html")

    def test_privacypage_contains_correct_html(self):
        self.assertContains(self.response, "Privacy")

    def test_privacypage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_privacypage_url_resolves_privacypageview(self):
        view = resolve("/privacy/")
        self.assertEqual(view.func.__name__, PrivacyPageView.as_view().__name__)
