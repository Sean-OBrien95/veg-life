from .models import UserProfile, Comment, Post
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_summernote.widgets import SummernoteWidget
from django.core.validators import MaxLengthValidator


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'excerpt', 'featured_image']

        widgets = {
            'content': SummernoteWidget(),
    }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].validators.append(MaxLengthValidator(
            limit_value=25, message='Title must be 25 characters or fewer.'))


class LikeCommentForm(forms.Form):
    comment_id = forms.IntegerField()


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class ProfileForm(forms.ModelForm):

    VEGAN_DURATION_CHOICES = [
        ('0-6 months', '0-6 months'),
        ('6-12 months', '6-12 months'),
        ('1-2 years', '1-2 years'),
        ('2-3 years', '2-3 years'),
        ('3-5 years', '3-5 years'),
        ('5+ years', '5+ years'),
    ]

    vegan_duration = forms.ChoiceField(choices=VEGAN_DURATION_CHOICES, required=False)

    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture',
                  'vegan_duration', 'favorite_animal', 'interests']

