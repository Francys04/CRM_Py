from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.messages import get_messages
from lead.models import Lead
from team.models import Team
from clients.models import Client as Client1

class LeadViewTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a related Team instance for the test user
        self.team = Team.objects.create(name='Test Team', created_by=self.user)

        # Create a test lead with the related team
        self.lead = Lead.objects.create(name='Test Lead', email='test@example.com', team=self.team, create_by=self.user)

        # Create a Django test client
        self.client = Client()

    def test_leads_list(self):
        # Log in the test user
        self.client.login(username='testuser', password='testpassword')

        # Send a GET request to the leads_list view
        response = self.client.get(reverse('leads_list'))

        # Check that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check that the response context contains the leads
        self.assertIn('leads', response.context)

        # Check that the leads in the context match the created lead
        leads = response.context['leads']
        self.assertEqual(len(leads), 1)
        self.assertEqual(leads[0].name, 'Test Lead')

        # Check that there are no messages in the context
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 0)

    def test_leads_delete(self):
        # Log in the test user
        self.client.login(username='testuser', password='testpassword')

        # Send a POST request to the leads_delete view with the lead's pk
        response = self.client.post(reverse('leads_delete', args=[self.lead.pk]))

        # Check that the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)

        # Check that the lead was deleted
        self.assertEqual(Lead.objects.count(), 0)

        # Check that a success message was added to the messages framework
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'The lead was deleted !')


class ConvertToClientViewTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a related Team instance for the test user
        self.team = Team.objects.create(name='Test Team', created_by=self.user)

        # Create a test lead with the related team
        self.lead = Lead.objects.create(name='Test Lead', email='test@example.com', team=self.team, create_by=self.user)

        # Create a Django test client
        self.client = Client()

    def test_convert_to_client(self):
        # Log in the test user
        self.client.login(username='testuser', password='testpassword')

        # Send a POST request to the convert_to_client view with the lead's pk
        response = self.client.post(reverse('leads_convert', args=[self.lead.pk]))

        # Check that the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)

        # Check that the lead is converted to a client
        client = Client1.objects.get(name='Test Lead')
        self.assertIsNotNone(client)
        self.assertEqual(client.email, 'test@example.com')
        self.assertEqual(client.description, self.lead.description)
        self.assertEqual(client.create_by, self.user)
        self.assertEqual(client.team, self.team)

        # Check that the lead's converted_to_client field is True
        lead = Lead.objects.get(pk=self.lead.pk)
        self.assertTrue(lead.converted_to_client)

        # Check that a success message was added to the messages framework
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'This lead was converted to the client')

        # Check that the view redirects to the leads_list page
        self.assertRedirects(response, reverse('leads_list'))