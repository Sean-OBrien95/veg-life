from .models import UserProfile, Comment, Post
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'excerpt', 'featured_image']

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio']
