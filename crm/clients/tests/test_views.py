from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from clients.models import Client
from team.models import Team

class ClientsViewsTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )

        # Create a test team
        self.team = Team.objects.create(name='Test Team', created_by=self.user)

        # Create some test clients
        self.client1 = Client.objects.create(
            team=self.team,
            name='Test Client 1',
            email='test1@example.com',
            create_by=self.user,
        )

        self.client2 = Client.objects.create(
            team=self.team,
            name='Test Client 2',
            email='test2@example.com',
            create_by=self.user,
        )

        # Set up the URL paths
        self.clients_list_url = reverse('clients_list')
        self.clients_detail_url = reverse('clients_detail', args=[self.client1.pk])

    def test_clients_list_view(self):
        # Log in the test user
        self.client.login(username='testuser', password='testpassword')

        # Send a GET request to the clients list view
        response = self.client.get(self.clients_list_url)

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert that the context contains the clients list
        self.assertIn('clients', response.context)
        self.assertEqual(len(response.context['clients']), 2)

    def test_clients_detail_view(self):
        # Log in the test user
        self.client.login(username='testuser', password='testpassword')

        # Send a GET request to the clients detail view
        response = self.client.get(self.clients_detail_url)

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert that the context contains the client instance
        self.assertIn('client', response.context)
        self.assertEqual(response.context['client'], self.client1)
