from django.test import TestCase

from .models import CustomUser


class CustomUserTests(TestCase):

    def test_create_user(self):
        user = CustomUser.objects.create_user(
            username="testuser",
            email="testuser@email.com",
            password="testpass123"
        )

        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        user = CustomUser.objects.create_superuser(
            username="testadmin",
            email="testadmin@email.com",
            password="testpass123"
        )

        self.assertEqual(user.username, "testadmin")
        self.assertEqual(user.email, "testadmin@email.com")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)


