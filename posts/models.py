from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.text import slugify


# Defining choices of published or drafted
STATUS = ((0, "Draft"), (1, "Published"))

# Model for creating and keeping record of blog posts
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    tags = models.CharField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    class Meta:
        ordering = ['-created_on']


    def __str__(self):
        return self.title


    def number_of_likes(self):
        return self.likes.count()

# Model for comments on blog posts
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    commentor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_comments", null=True
    )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    likes = models.ManyToManyField(
        User, related_name='comment_likes', blank=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

# Custom user profile model, used to store information on profiles
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)
    vegan_duration = models.CharField(max_length=100, blank=True)
    favorite_animal = models.CharField(max_length=100, blank=True)
    interests = models.TextField(blank=True)


    def __str__(self):
        return self.user.username

# Model for tracking bookmarked posts
class Bookmark(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='bookmarks')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
