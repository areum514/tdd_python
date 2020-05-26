from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
# Create your tests here.
from lists.views import home_page


class HomePageTest(TestCase):
    def test_root_url_reverse_to_home_pabe_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        print(response)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
