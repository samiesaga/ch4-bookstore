from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve
from .forms import CustomUserCreationForm
from .urls import SignupPageView
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

class SignupPageTests(TestCase):
    def setUp(self):
        url = reverse("signup")
        self.response = self.client.get(url)
    
    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "account/signup.html")
        self.assertContains(self.response, "Sign Up")
        self.assertNotContains(self.response, "hi there I should not be here")

    def test_signup_form(self):
        form = self.response.context.get('form')
    
        self.assertContains(self.response, "csrfmiddlewaretoken")

    def test_signup_view(self):
        view = resolve("/accounts/signup/")
        self.assertEqual(view.func.__name__, SignupPageView.as_view().__name__)


    