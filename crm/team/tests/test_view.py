from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages.storage.fallback import FallbackStorage
from team.models import Team
from team.forms import TeamForm
from team.views import edit_team

class EditTeamViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.team = Team.objects.create(
            plan_id=1,
            name='Test Team',
            created_by=self.user,
        )

    def test_edit_team_view_with_valid_data(self):
        form_data = {
            'name': 'Updated Team',
        }
        url = reverse('edit_team', args=[self.team.pk])
        request = self.factory.post(url, data=form_data)
        request.user = self.user
        # Required to use messages in the view
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)

        response = edit_team(request, pk=self.team.pk)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('myaccount'))
        self.team.refresh_from_db()
        self.assertEqual(self.team.name, 'Updated Team')
        self.assertEqual(str(response.wsgi_request._messages), '[]')

    def test_edit_team_view_with_invalid_data(self):
        form_data = {
            'name': '',  # Empty name, which is invalid
        }
        url = reverse('edit_team', args=[self.team.pk])
        request = self.factory.post(url, data=form_data)
        request.user = self.user
        # Required to use messages in the view
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)

        response = edit_team(request, pk=self.team.pk)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'team/templates/team/edit_team.html')
        self.assertFormError(response, 'form', 'name', 'This field is required.')
        self.team.refresh_from_db()
        self.assertEqual(self.team.name, 'Test Team')
        self.assertIn('This field is required.', str(response.content))
        self.assertEqual(str(response.wsgi_request._messages), '[]')
