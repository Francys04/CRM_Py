"""The django.test.TestCase class is a subclass of Django's unittest.
TestCase and provides additional features and utilities to simplify testing of Django applications."""
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages

from team.models import Team, Plan
from team.forms import TeamForm

class EditTeamViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.plan = Plan.objects.create(name='Test Plan', price=100, max_leads=10, max_clients=5)
        self.team = Team.objects.create(name='Test Team', plan=self.plan, created_by=self.user)

    def test_edit_team(self):
        # Simulate a POST request to the edit_team view
        self.client.login(username='testuser', password='testpassword')
        url = reverse('edit_team', args=[self.team.pk])
        data = {'name': 'New Team Name'}
        response = self.client.post(url, data)

        # Assert that the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)

        # Check that the team name has been updated in the database
        self.team.refresh_from_db()
        self.assertEqual(self.team.name, 'New Team Name')

        # Check that a success message is displayed
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'The changes was saved!')

    def test_edit_team_form_invalid(self):
        # Simulate a POST request with invalid data to the edit_team view
        self.client.login(username='testuser', password='testpassword')
        url = reverse('edit_team', args=[self.team.pk])
        data = {'name': ''}
        response = self.client.post(url, data)

        # Assert that the response status code is 200 (form validation failed)
        self.assertEqual(response.status_code, 200)

        # Check that the team name remains unchanged in the database
        self.team.refresh_from_db()
        self.assertEqual(self.team.name, 'Test Team')
        
    def test_edit_team_get(self):
        # Simulate a GET request to the edit_team view
        self.client.login(username='testuser', password='testpassword')
        url = reverse('edit_team', args=[self.team.pk])
        response = self.client.get(url)

        # Assert that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check that the form in the response contains the correct initial data
        form = response.context['form']
        self.assertIsInstance(form, TeamForm)
        self.assertEqual(form.initial['name'], 'Test Team')

    def test_edit_team_not_found(self):
        # Simulate a GET request to the edit_team view with an invalid team pk
        self.client.login(username='testuser', password='testpassword')
        url = reverse('edit_team', args=[999])  # 999 is an invalid team pk
        response = self.client.get(url)

        # Assert that the response status code is 404 (team not found)
        self.assertEqual(response.status_code, 404)



