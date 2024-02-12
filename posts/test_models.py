from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment, UserProfile, Bookmark


"""
Creating a post for and liking it for testing
"""
class PostModelTest(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='test@example.com'
        )

    def test_post_model_creation(self):
        post = Post.objects.create(
            title='Test Post',
            content='This is a test post content.',
            author=self.user,
            status=1,
        )
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(post.author, self.user)
        self.assertEqual(post.status, 1)
        self.assertEqual(str(post), 'Test Post')

    def test_post_model_likes(self):
        post = Post.objects.create(
            title='Test Post',
            content='This is a test post content.',
            author=self.user,
            status=1,
        )
        user_liking_post = User.objects.create_user(
            username='liker',
            password='testpassword',
            email='liker@example.com'
        )
        post.likes.add(user_liking_post)
        self.assertEqual(post.number_of_likes(), 1)


"""
Creating  apost and commenting for test purposes
"""
class CommentModelTest(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='test@example.com'
        )
        # Create a post for testing
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post content.',
            author=self.user,
            status=1,
        )

    def test_comment_model_creation(self):
        comment = Comment.objects.create(
            post=self.post,
            commentor=self.user,
            name='Test Commentor',
            email='test@example.com',
            body='This is a test comment body.',
            approved=True,
        )
        self.assertEqual(comment.post, self.post)
        self.assertEqual(comment.commentor, self.user)
        self.assertEqual(comment.body, 'This is a test comment body.')
        self.assertEqual(str(comment),
                         'Comment This is a test comment body. by Test Commentor')


"""
Testing the users profile
"""
class UserProfileModelTest(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='test@example.com'
        )

    def test_user_profile_model_creation(self):
        user_profile = UserProfile.objects.create(
            user=self.user,
            bio='This is a test bio.',
            vegan_duration='1-2 years',
            favorite_animal='Elephant',
            interests='Coding, Reading',
        )
        self.assertEqual(user_profile.user, self.user)
        self.assertEqual(user_profile.bio, 'This is a test bio.')
        self.assertEqual(user_profile.vegan_duration, '1-2 years')
        self.assertEqual(user_profile.favorite_animal, 'Elephant')
        self.assertEqual(user_profile.interests, 'Coding, Reading')
        self.assertEqual(str(user_profile), 'testuser')


"""
Testing functionality of the bookmark model
"""
class BookmarkModelTest(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='test@example.com'
        )
        # Create a post for testing
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post content.',
            author=self.user,
            status=1,
        )

    def test_bookmark_model_creation(self):
        bookmark = Bookmark.objects.create(user=self.user, post=self.post)
        self.assertEqual(bookmark.user, self.user)
        self.assertEqual(bookmark.post, self.post)
