from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse("user:create")
TOKEN_URL = reverse("user:token")


def create_user(**parameters):
    return get_user_model().objects.create_user(**parameters)


class PublicUserApiTests(TestCase):
    """Test the user API (public)"""

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_successful(self):
        """Test creating user with valid payload is successful"""
        payload = {
            "email": "test@test.com",
            "password": "TestPassword123",
            "name": "Test name"
        }
        response = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**response.data)
        self.assertTrue(user.check_password(payload["password"]))
        self.assertNotIn("password", response.data)

    def test_user_exists(self):
        """Test creating user that already exists fails"""
        payload = {
            "email": "test@test.com",
            "password": "TestPassword123",
        }
        create_user(**payload)

        response = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """Test that the password must be more than 5 characters"""

        payload = {
            "email": "test@test.com",
            "password": "pw",
        }

        response = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email=payload["email"]
        ).exists()
        self.assertFalse(user_exists)

    def test_create_token_for_user(self):
        """Test that a token is created for the user"""
        payload = {"email": "test@test.com", "password": "TestPassword123"}
        create_user(**payload)
        response = self.client.post(TOKEN_URL, payload)

        self.assertIn("token", response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_token_no_user(self):
        """Test that token is not created if user doesn't exists"""
        payload = {"email": "test@test.com", "password": "TestPassword123"}
        response = self.client.post(TOKEN_URL, payload)

        self.assertNotIn("token", response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_missing_field(self):
        """Test that email and password are required"""
        response = self.client.post(
            TOKEN_URL, {"email": "one", "password": ""}
        )
        self.assertNotIn("token", response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
