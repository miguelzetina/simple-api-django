from django.contrib.auth import get_user_model
from django.test import TestCase


class UserModelsTestCase(TestCase):
    """
    Tests for the user models module.
    """

    def setUp(self):
        self.user_model = get_user_model()
        self.user = self.user_model.objects.create_superuser(
            username='user',
            email='user@email.com',
            password='secret'
        )

    def test_user_model(self):
        email = 'user@email.com'
        user = self.user_model.objects.get(email=email)

        self.assertEqual(user.email, email)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_active)

