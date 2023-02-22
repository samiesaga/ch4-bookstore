from django.contrib.auth import get_user_model
from django.test import TestCase
# Create your tests here.


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username = "chapter4", email = "chapter4gmail.com", password = "chapter4"
        )
        self.assertEqual(user.username, "chapter4")
        self.assertEqual(user.email, "chapter4gmail.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFasle(user.is_superuser)

    def test_create_user(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username = "superadmin", email = "superadmingmail.com", password = "superadmin"
        )
        self.assertEqual(admin_user.username, "superadmin")
        self.assertEqual(admin_user.email, "superadmingmail.com")
        self.assertTrue( admin_user.is_active)
        self.assertTrue( admin_user.is_staff)
        self.assertTrue( admin_user.is_superuser)