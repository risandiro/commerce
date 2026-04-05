from django.test import Client, TestCase
from django.urls import reverse


class PublicPageTests(TestCase):
    """Smoke tests: main routes respond without server errors."""

    def setUp(self):
        self.client = Client()

    def test_index_returns_200(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_login_page_returns_200(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    def test_register_page_returns_200(self):
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)

    def test_categories_returns_200(self):
        response = self.client.get(reverse("categories"))
        self.assertEqual(response.status_code, 200)
