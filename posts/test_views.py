from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Comment, Bookmark, UserProfile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404


"""
Testing functionality of the views.py
"""
class ViewTests(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        # Create a test post
        self.post = Post.objects.create(
            title='Test Post',
            content='Test content',
            author=self.user,
            status=1
        )

    """
    Test the post list view with a search query.
    """
    def test_post_list_view_with_search_query(self):
        response = self.client.get(reverse('post_list'), {'q': 'Test'})
        self.assertEqual(response.status_code, 200)

    """
    Test the post like view.
    """
    def test_post_like_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(
            reverse('post_like', args=[self.post.slug]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(self.post.likes.filter(id=self.user.id).exists())

    """
    Test the edit profile view.
    """
    def test_edit_profile_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('edit_profile'), {
            'field_to_edit': 'new_value',
        })
        self.assertEqual(response.status_code, 302)

    """
    Test the user bookmarks view.
    """
    def test_user_bookmarks_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('user_bookmarks'))
        self.assertEqual(response.status_code, 200)

    """
    Test the post detail view.
    """
    def test_post_detail_view(self):
        response = self.client.get(
            reverse('post_detail', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)

    """
    Test the post detail view with POST method.
    """
    def test_post_detail_view_post_method(self):
        response = self.client.post(
            reverse('post_detail', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)

    """
    Test the post detail view with comment POST method.
    """
    def test_post_detail_view_comment_post_method(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(
            reverse('post_detail', args=[self.post.slug]), {})
        self.assertEqual(response.status_code, 200)

    """
    Test the post detail view with an invalid slug.
    """
    def test_post_detail_view_invalid_slug(self):
        response = self.client.get(
            reverse('post_detail', args=['invalid-slug']))
        self.assertEqual(response.status_code, 404)

    """
    Test the confirm delete view.
    """
    def test_confirm_delete_view(self):
        response = self.client.get(
            reverse('confirm_delete', args=[self.post.slug]))
        self.assertEqual(response.status_code, 403)

    """
    Test the confirm profile delete view.
    """
    def test_confirm_profile_delete_view(self):
        response = self.client.get(reverse('confirm_profile_delete'))
        self.assertEqual(response.status_code, 302)

    """
    Test the delete profile view.
    """
    def test_delete_profile_view(self):
        response = self.client.get(
            reverse('delete_profile', args=[self.user.id]))
        self.assertEqual(response.status_code, 302)

    """
    Test the delete profile view with unauthorized access.
    """
    def test_delete_profile_view_unauthorized(self):
        unauthorized_user = User.objects.create_user(
            username='unauthorized',
            password='unauthorizedpassword'
        )
        self.client.login(
            username='unauthorized', password='unauthorizedpassword')
        response = self.client.get(
            reverse('delete_profile', args=[self.user.id]))
        self.assertEqual(response.status_code, 302)

    """
    Test the delete comment view.
    """
    def test_delete_comment_view(self):
        comment = Comment.objects.create(
            post=self.post,
            commentor=self.user,
            body='Test Comment'
        )
        response = self.client.get(
            reverse('delete_comment', args=[comment.id]))
        self.assertEqual(response.status_code, 302)

    """
    Test the delete comment view with unauthorized access.
    """
    def test_delete_comment_view_unauthorized(self):
        unauthorized_user = User.objects.create_user(
            username='unauthorized',
            password='unauthorizedpassword'
        )
        self.client.login(
            username='unauthorized', password='unauthorizedpassword')
        comment = Comment.objects.create(
            post=self.post,
            commentor=self.user,
            body='Test Comment'
        )
        response = self.client.get(
            reverse('delete_comment', args=[comment.id]))
        self.assertEqual(response.status_code, 302)

    """
    Test the comment approval view.
    """
    def test_comment_approval_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('comment_approval'))
        self.assertEqual(response.status_code, 302)

    """
    Test the comment approval view with superuser access.
    """
    def test_comment_approval_view_superuser(self):
        superuser = User.objects.create_superuser(
            username='superuser',
            password='superuserpassword'
        )
        self.client.login(username='superuser', password='superuserpassword')
        response = self.client.get(reverse('comment_approval'))
        self.assertEqual(response.status_code, 200)

    """
    Test the toggle bookmark view.
    """
    def test_toggle_bookmark_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(
            reverse('toggle_bookmark', args=[self.post.id]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Bookmark.objects.filter(user=self.user, post=self.post).exists())

    """
    Test the user bookmarks view with unauthenticated access.
    """
    def test_user_bookmarks_view_unauthenticated(self):
        response = self.client.get(reverse('user_bookmarks'))
        self.assertEqual(response.status_code, 302)

    """
    Test the confirm delete view with unauthorized access.
    """
    def test_confirm_delete_view_unauthorized(self):
        unauthorized_user = User.objects.create_user(
            username='unauthorized',
            password='unauthorizedpassword'
        )
        self.client.login(
            username='unauthorized', password='unauthorizedpassword')
        response = self.client.get(
            reverse('confirm_delete', args=[self.post.slug]))
        self.assertEqual(response.status_code, 403)

    """
    Test the confirm profile delete view with unauthenticated access.
    """
    def test_confirm_profile_delete_view_unauthenticated(self):
        response = self.client.get(reverse('confirm_profile_delete'))
        self.assertEqual(response.status_code, 302)
