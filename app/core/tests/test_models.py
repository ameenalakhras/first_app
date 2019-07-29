from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successfully(self):
        """Test creating a new user with an email is successful"""
        email = "test@test.com"
        password = "TestPassword123"
        user = get_user_model()
        new_user = user.objects.create_user(
            email=email,
            password=password
        )

        # check email and password are equal to what is saved
        self.assertEqual(new_user.email, email)
        self.assertTrue(new_user.check_password(password))
