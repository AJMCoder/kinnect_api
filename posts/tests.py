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


class PostDetailViewTests(APITestCase):
    def setUp(self):
        test = User.objects.create_user(username='testuser', password='testpassword')
        Post.objects.create(owner=test, title='Test Post', content='Test Content')

    def test_can_retrieve_post_using_valid_id(self):
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['title'], 'Test Post')
        self.assertEqual(response.data['content'], 'Test Content')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_retrieve_post_using_invalid_id(self):
        response = self.client.get('/posts/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_logged_in_user_can_update_own_post(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.put('/posts/1/', {'title': 'Updated Post', 'content': 'Updated Content'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Post')
        self.assertEqual(response.data['content'], 'Updated Content')

    def test_logged_in_user_cannot_update_other_users_post(self):
        test2 = User.objects.create_user(username='testuser2', password='testpassword')
        self.client.login(username='testuser2', password='testpassword')
        response = self.client.put('/posts/1/', {'title': 'Updated Post', 'content': 'Updated Content'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)