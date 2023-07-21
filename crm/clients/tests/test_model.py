# clients/tests.py
from django.test import TestCase
from clients.models import Client
from team.models import Team, Plan
from django.contrib.auth.models import User

class ClientModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # Create a Plan instance with max_clients, max_leads, and price
        self.plan = Plan.objects.create(name='Test Plan', description='Test Description', max_clients=10, max_leads=100, price=10.0)
        # Use the created Plan instance when creating the Team instance
        self.team = Team.objects.create(name='Test Team', created_by=self.user, plan=self.plan)
        self.client = Client.objects.create(
            team=self.team,
            name='Test Client',
            email='test@example.com',
            create_by=self.user,
        )

    def test_client_model_str(self):
        self.assertEqual(str(self.client), 'Test Client')

    def test_client_model_ordering(self):
        # Create another client with a different name
        client2 = Client.objects.create(
            team=self.team,
            name='Test Client',
            email='another_test@example.com',
            create_by=self.user,
        )
        # Test ordering by name, should be alphabetical
        clients = Client.objects.all()
        self.assertEqual(clients[0], self.client)
        self.assertEqual(clients[1], client2)
    
    
