from django.test import SimpleTestCase
from django.urls import reverse, resolve

from pages.views import TermsPageView


class TermsPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("pages:terms")
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_termspage_template(self):
        self.assertTemplateUsed(self.response, "pages/terms.html")

    def test_termspage_contains_correct_html(self):
        self.assertContains(self.response, "Terms")

    def test_termspage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_termspage_url_resolves_termspageview(self):
        view = resolve("/terms/")
        self.assertEqual(view.func.__name__, TermsPageView.as_view().__name__)
