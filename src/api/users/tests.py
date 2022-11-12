from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status


class RegisterUserTest(APITestCase):
    """Test cases for Register User APIs"""
    def setUp(self):
        self.test_user = User.objects.create_user('testuser', 'test@example.com', 'testpassword')
        self.create_url = reverse('register')

    def test_create_user(self):
        """
        Ensure we can create a new user and a valid token is created with it.
        """
        data = {
            'username': 'foobar',
            'email': 'foobar@example.com',
            'password': 'somepassword'
        }

        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], data['username'])
        self.assertEqual(response.data['email'], data['email'])
        self.assertFalse('password' in response.data)

    def test_create_user_with_short_password(self):
        """
        Ensure user is not created for password lengths less than 8.
        """
        data = {
                'username': 'foobar',
                'email': 'foobarbaz@example.com',
                'password': 'foo'
        }

        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['password']), 1)

    def test_create_user_with_no_password(self):
        """
        Ensure user is not created if no password is provided.
        """
        data = {
                'username': 'foobar',
                'email': 'foobarbaz@example.com',
                'password': ''
        }

        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['password']), 1)

    def test_create_user_with_too_long_username(self):
        """
        Ensure user is not created if username is length than set limit.
        """
        data = {
            'username': 'foo'*30,
            'email': 'foobarbaz@example.com',
            'password': 'foobar1021'
        }

        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['username']), 1)

    def test_create_user_with_preexisting_username(self):
        """
        Ensure user is not created if no username already exists.
        """
        data = {
                'username': 'testuser',
                'email': 'user@example.com',
                'password': 'testuser'
                }

        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['username']), 1)

    def test_create_user_with_preexisting_email(self):
        """
        Ensure user is not created if no email already exists.
        """
        data = {
            'username': 'testuser2',
            'email': 'test@example.com',
            'password': 'testuser'
        }

        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['email']), 1)

    def test_create_user_with_invalid_email(self):
        """
        Ensure user is not created if email is invalid
        """
        data = {
            'username': 'foobarbaz',
            'email':  'testing',
            'passsword': 'foobarbaz'
        }

        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['email']), 1)


class LoginTest(APITestCase):
    """Test cases for Login API"""
    def setUp(self):
        self.test_user = User.objects.create_user('testuser', 'test@example.com', 'testpassword')
        self.login_url = reverse('login')

    def test_login_user_correct_creds(self):
        """
        Ensure we can login a user and receive token as response.
        """
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }

        response = self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('expiry' in response.data)
        self.assertTrue('token' in response.data)

    def test_login_user_wrong_password(self):
        """
        Ensure we can login a user and receive token as response.
        """
        data = {
            'username': 'testuser',
            'password': 'testpass'
        }

        response = self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


# TODO
# Add Below Unit Test Cases:
# 1. Positive and Negative test cases for Logout API

