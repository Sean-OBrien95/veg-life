from .models import UserProfile, Comment, Post
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_summernote.widgets import SummernoteWidget
from django.core.validators import MaxLengthValidator
from allauth.account.forms import LoginForm


"""
Define a form for comments
"""
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


"""
Define a form for creating posts
"""
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'excerpt', 'featured_image']

        # Use SummernoteWidget for the 'content' field
        widgets = {
            'content': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        # Add a validator for the 'title' field
        self.fields['title'].validators.append(MaxLengthValidator(
            limit_value=25, message='Title must be 25 characters or fewer.'))


"""
Define a form for liking a comment
"""
class LikeCommentForm(forms.Form):
    comment_id = forms.IntegerField()


"""
Define a registration form extending UserCreationForm
"""
class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


"""
Define a form for user details
"""
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


"""
Define a form for user profile details
"""
class ProfileForm(forms.ModelForm):

    VEGAN_DURATION_CHOICES = [
        ('0-6 months', '0-6 months'),
        ('6-12 months', '6-12 months'),
        ('1-2 years', '1-2 years'),
        ('2-3 years', '2-3 years'),
        ('3-5 years', '3-5 years'),
        ('5+ years', '5+ years'),
    ]

    vegan_duration = forms.ChoiceField(
            choices=VEGAN_DURATION_CHOICES, required=False)

    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture',
                  'vegan_duration', 'favorite_animal', 'interests']


"""
Define a custom login form extending LoginForm
"""
class MyCustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove help text for the 'password' field, forgotten password link
        self.fields["password"].help_text = None
