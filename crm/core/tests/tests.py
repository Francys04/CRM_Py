"""The django.test.TestCase class is a subclass of Django's unittest.
TestCase and provides additional features and utilities to simplify testing of Django applications."""
from django.test import TestCase
"""The reverse function is a powerful utility that allows you to generate URLs for named URL 
patterns defined in your Django application's urls.py files."""
from django.urls import reverse

"""Core view test contains two test methods to test the behavior of the index and about views in your Django application."""
class CoreViewsTestCase(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/index.html')

    def test_about_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/about.html')

