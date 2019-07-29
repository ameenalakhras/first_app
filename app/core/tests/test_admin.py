from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTest(TestCase):

    # setUp function runs before all test functions
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@admin.com",
            password="password123"
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="test@test.com",
            password="password123",
            name="Test user full name"
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""
        # reverse : generate a url for the (app_you_want:url_you_want)
        url = reverse("admin:core_user_changelist")
        # (res:response), (get(url) :test user perform http request on a url)
        res = self.client.get(url)
        # assertContains : checks if it's 200 response + checks if
        # second variable is part of the first variable
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_page_change(self):
        """Test that the user edit page works"""
        # the next line will generate "0.0.0.0:8000/admin/core/user/1"
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
