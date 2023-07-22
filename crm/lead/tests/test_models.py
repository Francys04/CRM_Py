"""The django.test.TestCase class is a subclass of Django's unittest.
TestCase and provides additional features and utilities to simplify testing of Django applications."""
from django.test import TestCase
from django.contrib.auth.models import User
from team.models import Team
from lead.models import Lead

class LeadModelTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a team for the test user
        self.team = Team.objects.create(name='Test Team', created_by=self.user)

    def test_lead_creation(self):
        # Create a lead for testing
        lead = Lead.objects.create(
            team=self.team,
            name='Test Lead',
            email='test@example.com',
            description='Test description',
            priority=Lead.LOW,
            status=Lead.NEW,
            create_by=self.user
        )

        # Check that the lead was created successfully
        self.assertEqual(lead.team, self.team)
        self.assertEqual(lead.name, 'Test Lead')
        self.assertEqual(lead.email, 'test@example.com')
        self.assertEqual(lead.description, 'Test description')
        self.assertEqual(lead.priority, Lead.LOW)
        self.assertEqual(lead.status, Lead.NEW)
        self.assertEqual(lead.converted_to_client, False)
        self.assertEqual(lead.create_by, self.user)

    def test_lead_str_method(self):
        # Create a lead for testing
        lead = Lead.objects.create(
            team=self.team,
            name='Test Lead',
            email='test@example.com',
            create_by=self.user
        )

        # Check that the __str__ method returns the correct name of the lead
        self.assertEqual(str(lead), 'Test Lead')

    def test_lead_ordering(self):
        # Create multiple leads with different names for testing ordering
        lead1 = Lead.objects.create(team=self.team, name='Lead C', email='test1@example.com', create_by=self.user)
        lead2 = Lead.objects.create(team=self.team, name='Lead A', email='test2@example.com', create_by=self.user)
        lead3 = Lead.objects.create(team=self.team, name='Lead B', email='test3@example.com', create_by=self.user)

        # Get all leads ordered by name
        ordered_leads = Lead.objects.all()

        # Check that the leads are ordered alphabetically by name
        self.assertEqual(ordered_leads[0], lead2)
        self.assertEqual(ordered_leads[1], lead3)
        self.assertEqual(ordered_leads[2], lead1)
