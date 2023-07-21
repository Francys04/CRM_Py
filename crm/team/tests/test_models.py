from django.test import TestCase
from django.contrib.auth.models import User
from team.models import Plan, Team

class PlanModelTestCase(TestCase):
    def setUp(self):
        self.plan = Plan.objects.create(
            name='Basic Plan',
            price=50,
            description='This is the basic plan',
            max_leads=100,
            max_clients=50,
        )

    def test_plan_str_method(self):
        self.assertEqual(str(self.plan), 'Basic Plan')

    def test_plan_attributes(self):
        self.assertEqual(self.plan.name, 'Basic Plan')
        self.assertEqual(self.plan.price, 50)
        self.assertEqual(self.plan.description, 'This is the basic plan')
        self.assertEqual(self.plan.max_leads, 100)
        self.assertEqual(self.plan.max_clients, 50)


class TeamModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.plan = Plan.objects.create(
            name='Basic Plan',
            price=50,
            description='This is the basic plan',
            max_leads=100,
            max_clients=50,
        )
        self.team = Team.objects.create(
            plan=self.plan,
            name='Test Team',
            created_by=self.user,
        )
        self.team.memebers.add(self.user)

    def test_team_str_method(self):
        self.assertEqual(str(self.team), 'Test Team')

    def test_team_attributes(self):
        self.assertEqual(self.team.plan, self.plan)
        self.assertEqual(self.team.name, 'Test Team')
        self.assertEqual(self.team.created_by, self.user)
        self.assertEqual(self.team.memebers.count(), 1)
        self.assertIn(self.user, self.team.memebers.all())
