from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import User

class AuthenticationTests(APITestCase):
    """
    Test suite for user authentication endpoints.
    """

    def setUp(self):
        """
        Set up initial data for tests.
        """
        self.register_url = reverse('user-registration')
        self.login_url = reverse('token_obtain_pair')
        self.refresh_url = reverse('token_refresh')
        
        self.user_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'password': 'strong-password123'
        }

    #Registration Tests

    def test_user_registration_success(self):
        """
        Ensure a new user can be registered successfully.
        """
        response = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().email, self.user_data['email'])
        self.assertNotIn('password', response.data)

    def test_user_registration_fail_duplicate_email(self):
        """
        Ensure registration fails if the email already exists.
        """
        self.client.post(self.register_url, self.user_data, format='json')
        
        response = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)

    #Login Tests

    def test_user_login_success(self):
        """
        Ensure a registered user can log in and receive tokens.
        """
        self.client.post(self.register_url, self.user_data, format='json')
        
        login_data = {
            'email': self.user_data['email'],
            'password': self.user_data['password']
        }
        response = self.client.post(self.login_url, login_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self


    def test_user_login_fail_wrong_password(self):
        """
        Ensure login fails with an incorrect password.
        """
        
        self.client.post(self.register_url, self.user_data, format='json')
        
        login_data = {
            'email': self.user_data['email'],
            'password': 'wrong-password'
        }
        response = self.client.post(self.login_url, login_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_login_fail_nonexistent_user(self):
        """
        Ensure login fails for a user that does not exist.
        """
        login_data = {
            'email': 'nobody@example.com',
            'password': 'a-password'
        }
        response = self.client.post(self.login_url, login_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # --- Token Refresh Test ---

    def test_token_refresh_success(self):
        """
        Ensure a valid refresh token can be used to get a new access token.
        """
        self.client.post(self.register_url, self.user_data, format='json')
        login_response = self.client.post(self.login_url, {
            'email': self.user_data['email'],
            'password': self.user_data['password']
        }, format='json')
        
        refresh_token = login_response.data['refresh']
        
        response = self.client.post(self.refresh_url, {'refresh': refresh_token}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    def test_token_refresh_fail_invalid_token(self):
        """
        Ensure using an invalid refresh token fails.
        """
        response = self.client.post(self.refresh_url, {'refresh': 'invalid.token.string'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)