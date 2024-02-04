from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post
from .forms import PostForm

class CreatePostViewTest(TestCase):
    def setUp(self):
        # Create a superuser for testing
        self.user = User.objects.create_superuser(
            username='testuser', password='testpassword', email='test@example.com'
        )
        self.client.login(username='testuser', password='testpassword')

    def test_create_post_view_get(self):
        response = self.client.get(reverse('create_post'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_post.html')
        self.assertIsInstance(response.context['form'], PostForm)

    def test_create_post_view_post_valid(self):
        data = {
            'title': 'Test Post',
            'content': 'This is a test post content.',
            'excerpt': 'Test excerpt',
            'featured_image': 'test_image.jpg',
        }
        response = self.client.post(reverse('create_post'), data)
        self.assertEqual(response.status_code, 302)  # Redirects on successful post
        self.assertEqual(Post.objects.count(), 1)  # One post should be created

    def test_create_post_view_post_invalid(self):
        data = {}  # Invalid data, should trigger form validation errors
        response = self.client.post(reverse('create_post'), data)
        self.assertEqual(response.status_code, 200)  # Still on the same page
        self.assertTemplateUsed(response, 'create_post.html')
        self.assertIsInstance(response.context['form'], PostForm)
        self.assertContains(response, 'This field is required.')  # Example error message

from django.contrib.auth.models import User

class PostListViewTest(TestCase):
    def setUp(self):
        # Create a superuser for testing
        self.user = User.objects.create_superuser(
            username='testuser', password='testpassword', email='test@example.com'
        )
        self.client.login(username='testuser', password='testpassword')

    def test_post_list_view_with_posts(self):
        # Create some posts for testing with the specified author
        author = self.user
        Post.objects.create(title='Post 1', content='Content 1', status=1, author=author)
        Post.objects.create(title='Post 2', content='Content 2', status=1, author=author)

        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertQuerysetEqual(
            response.context['object_list'],
            ['<Post: Post 1>', '<Post: Post 2>'],
            ordered=False
        )

