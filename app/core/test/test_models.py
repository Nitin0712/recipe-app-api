from django.test import TestCase

from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_success(self):
        """test creating user with an email is successful"""
        email = "nitin@gmail.com"
        password = "nitin123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email(self):
        email = 'nitin@GMAIL.com'
        user = get_user_model().objects.create_user(email, 'nitin123')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test creating new user email validate"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'nitin123')

    def test_create_new_superuser(self):
        """Test create new super user"""
        user = get_user_model().objects.create_superuser(
            'neil_admin@gmail.com',
            'password123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
