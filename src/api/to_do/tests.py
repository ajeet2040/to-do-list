from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from to_do.models import ToDo


class ToDoTest(APITestCase):
    """Test cases for ToDo APIs"""
    def setUp(self):
        self.test_user = User.objects.create_user('testuser', 'test@example.com', 'testpassword')
        self.client.force_authenticate(self.test_user)
        self.todo_base = reverse('todo-list')

    def test_create_todo_valid_data(self):
        """
        Ensure we can create a new todo when valid data is passed.
        """
        data = {
            'title': 'foobar',
            'description': 'foobar@example.com',
            'is_completed': False
        }

        response = self.client.post(self.todo_base, data, format='json')
        self.assertEqual(ToDo.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.data['description'], data['description'])
        self.assertEqual(response.data['is_completed'], data['is_completed'])

    def test_create_todo_empty_title(self):
        """
        Ensure todo is not created for empty title.
        """
        data = {
            'title': '',
            'description': 'foobar@example.com',
            'is_completed': False
        }

        response = self.client.post(self.todo_base, data, format='json')
        self.assertEqual(ToDo.objects.count(), 0)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(len(response.data['title']), 1)


# TODO
# Add Below Unit Test Cases:
# 1. Create Todo for other invalid scenarios like no title, passing string in is_completed etc.
# 2. Positive and negative test cases for Fetch Todo List and Fetch Single Todo record (detail)
# 3. Positive and negative test cases for Fetch Todo Update and Todo Delete

# 4. Integration Test Case using token from Login API and creating ToDo record

