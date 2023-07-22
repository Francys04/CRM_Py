"""The django.test.TestCase class is a subclass of Django's unittest.
TestCase and provides additional features and utilities to simplify testing of Django applications."""
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from team.models import Team
from lead.models import Lead
from clients.models import Client

class DashboardViewTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_dashboard_view_with_leads_and_clients(self):
        # Create a team for the test user
        team = Team.objects.create(name='Test Team', created_by=self.user)

        # Create test leads and clients belonging to the team
        for i in range(10):
            Lead.objects.create(name=f'Test Lead {i}', email=f'test{i}@example.com', team=team, create_by=self.user)
            Client.objects.create(name=f'Test Client {i}', email=f'test{i}@example.com', team=team, create_by=self.user)

        # Log in the test user using the test client
        self.client.login(username='testuser', password='testpassword')

        # Make a GET request to the dashboard view
        response = self.client.get(reverse('dashboard'))

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the template used for rendering is 'dashboard/dashboard.html'
        self.assertTemplateUsed(response, 'dashboard/dashboard.html')

        # Check that the 'leads' context variable contains 5 leads
        self.assertEqual(len(response.context['leads']), 5)

        # Check that the 'clients' context variable contains 5 clients
        self.assertEqual(len(response.context['clients']), 5)

    def test_dashboard_view_with_no_leads_and_clients(self):
        # Create a team for the test user
        team = Team.objects.create(name='Test Team', created_by=self.user)

        # Log in the test user using the test client
        self.client.login(username='testuser', password='testpassword')

        # Make a GET request to the dashboard view
        response = self.client.get(reverse('dashboard'))

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the template used for rendering is 'dashboard/dashboard.html'
        self.assertTemplateUsed(response, 'dashboard/dashboard.html')

        # Check that the 'leads' context variable is empty
        self.assertQuerysetEqual(response.context['leads'], [])

        # Check that the 'clients' context variable is empty
        self.assertQuerysetEqual(response.context['clients'], [])
