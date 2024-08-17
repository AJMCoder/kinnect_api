from django.contrib.auth.models import User
from .models import Post
from rest_framework import status, permissions
from rest_framework.test import APITestCase

class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='testuser', password='testpassword')

    def test_can_list_posts(self):
        testuser = User.objects.get(username='testuser')
        Post.objects.create(owner=testuser, title='Test Post', content='Test Content')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_post(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post('/posts/', {'title': 'Test Post', 'content': 'Test Content'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cannot_create_post(self):
        response = self.client.post('/posts/', {'title': 'Test Post', 'content': 'Test Content'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)