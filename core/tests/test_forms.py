from django.test import TestCase
from django.contrib.auth.models import User
from core.forms import UserUpdateForm

class ProfileFormTests(TestCase):
    def test_valid_profile_form(self):
        user = User.objects.create_user(username='mahak', email='m@g.com')
        form = UserUpdateForm({'first_name': 'Mahak', 'last_name': 'G', 'email': 'new@g.com'}, instance=user)
        self.assertTrue(form.is_valid())
