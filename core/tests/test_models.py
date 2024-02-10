from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email and password"""
        email = "test@gmail.com"
        password = "cisco123"
        User = get_user_model()
        user = User.objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""       
        email = "test@gmail.com"
        password = "cisco123"
        User = get_user_model()
        user = User.objects.create_user(
            email="test@gmail.com",
            password="cisco123"
        )
        self.assertEqual(user.email, email.lower())

    def test_create_super_user(self):
        user = get_user_model().objects.create_superuser(
            email="test@gmail.com",
            password="test123"
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password="cisco123"
            )

