from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView, AboutMePageView

# Create your tests here.

class HomePageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_url_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Homepage')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'hi there')

    def test_homepage_url_resolve_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )

class AboutMePageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('about_me')
        self.response = self.client.get(url)

    def test_about_me_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_about_me_url_name(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_aboutme_url_resolve_aboutme(self):
        view = resolve('/about/')
        self.assertEqual(
            view.func.__name__, AboutMePageView.as_view().__name__
        )